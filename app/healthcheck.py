#sudo pmset -g thermlog gives the cpu_speed_limit which can be used to check cpu health
class ResourceHealth:
    def __init__(self,server):
        self._server=server
    def cpu_health_check(self,cpu_speed_limit: float)->str:
        if cpu_speed_limit < 70 and cpu_speed_limit>50:
            return "overheating"
        elif cpu_speed_limit<=50:
            return "overheated"
        return "healthy"

    #system_profiler SPMemoryDataType gives the RAM information- status ok indicates healthy
    def memory_health_check(self,memory_status: str)->str:
        if memory_status.casefold()=="ok":
            return "ok"
        return "notok"
        
    # diskutil info disk0 | grep -i smart gives the status of the disk
    def disk_health_check(self,smart_status: str)->str:
        if smart_status.casefold()=="verified":
            return "healthy"
        return "unhealthy"

    # battery status system_profiler SPPowerDataType | grep -A 3 -E "(Cycle Count|Condition)"
    def bat_health_check(self,condition: str)->str:
        if condition.casefold()=="normal":
            return "normal" 
        return "abnormal"
        
    #network errors  netstat -i 1 
    def net_health_check(self,ierrors: int,oerrrs: int )->str:
        if ierrors==0 and oerrrs==0:
            return "ok"
        return "notok"

    #check for system panic log show --predicate 'eventMessage CONTAINS "Panic"' --last 7d
    def sys_panic_check(self,panicerr:str)->str:
        if panicerr.casefold()=="panic":
            return "panic"
        return "nopanic"
        
    #sudo thermal levels
    def thermal_lev_check(self,cpu:int,gpu:int,io:int)->str:
        if cpu==0 and gpu==0 and io==0:
            return "normal"
        return "abnormal"