from wsgiref import headers
from app import app

def test_index_root():
    #thsi requests should fail not found as there is no route to root URI
    tester = app.test_client()
    response = tester.get("/", content_type="html/txt")
    assert response.status_code == 404

def test_api_root_get():
    #this request should not be permitted as we only want the POST requests
    tester = app.test_client()
    response = tester.get("/api", content_type="html/txt")
    assert response.status_code == 405

def test_api_post():
    #this request should be successfull
    tester  = app.test_client()
    data = {'comment': 'THis is comment'}
    response = tester.post("/api", data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    
