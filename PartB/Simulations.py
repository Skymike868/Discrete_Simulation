import numpy as np
import matplotlib.pylab as pylab
from PartB.FutureEventList import FutureEventList
from PartB.Customer import Customer
from PartB.Doctor import Doctor
from PartB.QueueEvent import QueueEvent, ARRIVAL, DEPARTURE


def sample_interarrival_time():
    return np.random.exponential(20)


# Standard deviation as 1 there data between 14 and 16

def sample_service_time():
    return np.random.normal(15, 1)


MAX_TIME_TO_SIMULATE = 24*60 # ONE day
event_list = FutureEventList()
first_arrival_time = sample_interarrival_time()
current_time = 0
next_arrival = current_time + first_arrival_time  # preparing for the new person
first_arrival = QueueEvent(first_arrival_time, ARRIVAL)
event_list.enqueue(first_arrival)
customers = []
curr_customer = 0
num_in_queue = 0
num_in_system = 0
doctor = Doctor()
service_time_array = []  # the time spent with the doctor
waiting_time_array = []  # the time spent in the waiting room
patient_total_time = []

while current_time < MAX_TIME_TO_SIMULATE:
    next_event = event_list.dequeue()
    current_time = next_event.get_time()
    if next_event.event_type == ARRIVAL:
        num_in_system += 1
        num_in_queue += 1
        service_time = sample_service_time()
        service_time_array.append(service_time)
        new_customer = Customer(current_time, service_time)
        customers.append(new_customer)
        next_arrival_time = current_time + sample_interarrival_time()
        next_arrival_event = QueueEvent(next_arrival_time, ARRIVAL)
        event_list.enqueue(next_arrival_event)
        if doctor.is_free():
            print('Serving customer...')
            waiting_time = current_time - (customers[curr_customer].arrival_time + 2)
            waiting_time_array.append(waiting_time)

            doctor.start_service(customers[curr_customer], current_time+2)
            departure_time = customers[curr_customer].service_time + current_time+2
            departure_event = QueueEvent(departure_time, DEPARTURE)

            num_in_queue -= 1
            event_list.enqueue(departure_event)
    elif next_event.event_type == DEPARTURE:
        num_in_system -= 1
        curr_customer += 1
        total_time = (current_time - doctor.current_customer.arrival_time) + 2
        patient_total_time.append(total_time)
        doctor.finish_serve(current_time)
        if num_in_queue > 0:#
            print('Serving customer...')
            waiting_time = current_time - (customers[curr_customer].arrival_time + 2)
            waiting_time_array.append(waiting_time)

            doctor.start_service(customers[curr_customer], current_time)
            departure_time = customers[curr_customer].service_time + current_time
            departure_event = QueueEvent(departure_time, DEPARTURE)
            num_in_queue -= 1
            event_list.enqueue(departure_event)

print("The Doctor's Active time", doctor.time_active)
print("The Doctor's Utilization time ",doctor.compute_utilization(MAX_TIME_TO_SIMULATE))
print("The Average total time spent", np.mean(patient_total_time))
print("Maximum Waiting time ", np.max(waiting_time_array))
print("Average Service Time", np.mean(service_time_array))
print("Maximum Service Time",np.max(service_time_array))
print("Minimum Service Time",np.min(service_time_array))

pylab.hist(waiting_time_array)
pylab.ylabel("Customer")
pylab.xlabel("Waiting time")
pylab.show()





