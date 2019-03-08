class TCP_Interface:

    def __init__(self, framework):
       self.framework = framework

    def ip_VMS(self, service_id, ip_list, id_list):
        self.framework.receive_ip_instantiated_service( service_id, ip_list, id_list )
        return True
    
    def add_sla(self, sla):
        return self.framework.add_single_SLA_network( sla )

    def new_monitoring_data(self, monitoring_data):
        return self.framework.new_monitoring_data( monitoring_data )

