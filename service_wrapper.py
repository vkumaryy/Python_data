import win32serviceutil
import win32service
import win32event
import servicemanager
from my_flask_app import app

class FlaskAppService(win32serviceutil.ServiceFramework):
    _svc_name_ = "FlaskAppService"
    _svc_display_name_ = "Flask App Service"
    _svc_description_ = "This service runs a Flask app."

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    def main(self):
        app.run()

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(FlaskAppService)



# python service_wrapper.py install



# python service_wrapper.py start

# python service_wrapper.py stop
    
# python service_wrapper.py remove

