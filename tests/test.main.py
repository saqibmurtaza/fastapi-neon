from fastapi.testclient import TestClient
from fastapi_neon import settings, app, get_session
from sqlmodel import create_engine, SQLModel, Session
######################################################################################
def test_read_root_todo():
    client = TestClient(app=app)
    gen_request_to_endpoint = client.get("/")
    assert gen_request_to_endpoint.status_code == 200
    assert gen_request_to_endpoint.json() == {"Hello": "My first API Endpoint"}
####################################################################################    
def test_post_todo():
    
    client = TestClient(app=app)

    connection_string = str(settings.TEST_DATABASE_URL).replace(
        "postgresql", "postgresql+psycopg"
    )
    engine = create_engine(connection_string, connect_args={"sslmode":"require"},
                           pool_recycle=300)
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        def get_session_override():
            return session
        app.dependency_overrides[get_session] = get_session_override

        todo_content = {"content": "buy eggs"}
        gen_request_to_endpoint = client.post("/todos/", json=todo_content)

        assert gen_request_to_endpoint.status_code == 200
        assert gen_request_to_endpoint.json() == todo_content
###########################################################################################
def test_read_todos_list():

    connection_string = str(settings.TEST_DATABASE_URL).replace(
        "postgresql", "postgresql+psycopg"
    )
    engine = create_engine(connection_string, connect_args={"sslmode":"require"},
                           pool_recycle=300)
    SQLModel.metadata.create_all(engine)

    client = TestClient(app=app)

    with Session(engine) as session:
        def get_session_override():
            return session
        app.dependency_overrides[get_session] = get_session_override

        gen_request_to_endpoint = client.get("/todos/")

        assert gen_request_to_endpoint.status_code == 200
        assert isinstance(gen_request_to_endpoint.json(), list)
#####################################################################################
def test_update_todo():

    client = TestClient(app)

    todo_content = {"content": "Buy milk"}

    response_add_todo = client.post("/todos/", json=todo_content)
    assert response_add_todo.status_code == 200

    # Extract the ID of the created todo
    created_todo_id = response_add_todo.json()["id"]

    # Prepare updated todo data
    updated_todo_data = {"content": "Buy milk and eggs"}

    # Update the todo item
    response_update_todo = client.put(f"/todos/{created_todo_id}", json=updated_todo_data)
    
    assert response_update_todo.status_code == 200
    assert response_update_todo.json()["content"] == updated_todo_data["content"]

    
#####################################################################################
def test_delete_todo():
    client = TestClient(app=app)

    connection_string = str(settings.TEST_DATABASE_URL).replace(
        "postgresql", "postgresql+psycopg"
    )
    engine = create_engine(connection_string, connect_args={"sslmode":"require"},
                           pool_recycle=300)
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        def get_session_override():
            return session
        app.dependency_overrides[get_session] = get_session_override

        todo_content = {"content": "buy eggs"}
        gen_request_to_add_todo = client.post("/todos/", json=todo_content)
        assert gen_request_to_add_todo.status_code == 200

        created_todo_id = gen_request_to_add_todo.json()["id"]

    gen_request_to_delete_todo = client.delete(f"/todos/{created_todo_id}")

    assert gen_request_to_delete_todo.status_code == 200
    assert gen_request_to_delete_todo.json() == {"message": "Todo deleted successfully"}
########################################################################################


