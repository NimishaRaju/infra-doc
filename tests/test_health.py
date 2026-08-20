from app.healthcheck import ResourceHealth
def test_health():
    t1=ResourceHealth("Milo")
    assert t1.cpu_health_check(40.2)==("overheated")
    assert t1.cpu_health_check(58.6)==("overheating")
    assert t1.cpu_health_check(79.6)==("healthy")
    assert t1.memory_health_check("OK")==("ok")
    assert t1.memory_health_check("ECC Errors")==("notok")
    assert t1.disk_health_check("Verified")==("healthy")
    assert t1.disk_health_check("Failing")==("unhealthy")