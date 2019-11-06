from prometheus_client import start_http_server,  Gauge
from temp import measure_temp


#sensor_file="c:\\Tmp\\28sens"
#metric
TEMPERATURE_RASPBERRYPI = Gauge('temperature_in_the_room', 'Temperature in celsius taken from sensor')
TEMPERATURE_RASPBERRYPI.set(measure_temp())
    

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    while True:
        measure_temp()