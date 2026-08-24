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
    assert t1.bat_health_check("Normal")==("normal")
    assert t1.bat_health_check("Failed")==("abnormal")
    assert t1.net_health_check(0,0)==("ok")
    assert t1.net_health_check(1,1)==("notok")
    assert t1.sys_panic_check("panic")==("panic")
    assert t1.sys_panic_check("")==("nopanic")
    assert t1.thermal_lev_check(0,0,0)==("normal")
    assert t1.thermal_lev_check(1,1,1)==("abnormal")
