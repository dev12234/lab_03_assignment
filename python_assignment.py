class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_by_flight_id(self, flight_id):
        for flight in self.flights:
            if flight.flight_id == flight_id:
                return flight
        return None

    def search_by_source(self, source):
        result = []
        for flight in self.flights:
            if flight.source == source:
                result.append(flight)
        return result

    def search_by_destination(self, destination):
        result = []
        for flight in self.flights:
            if flight.destination == destination:
                result.append(flight)
        return result

def main():
    flight_table = FlightTable()

    flight_table.add_flight(Flight("AI161E90", "BLR", "BOM", 5600))
    flight_table.add_flight(Flight("BR161F91", "BOM", "BBI", 6750))
    flight_table.add_flight(Flight("AI161F99", "BBI", "BLR", 8210))
    flight_table.add_flight(Flight("VS171E20", "JLR", "BBI", 5500))
    flight_table.add_flight(Flight("AS171G30", "HYD", "JLR", 4400))
    flight_table.add_flight(Flight("AI131F49", "HYD", "BOM", 3499))

    user_input = input("Enter flight ID, source city, or destination city: ")
    
    if len(user_input) == 8 and user_input.isalnum():
        flight = flight_table.search_by_flight_id(user_input)
        if flight:
            print(f"Flight ID: {flight.flight_id}, Source: {flight.source}, Destination: {flight.destination}, Price: {flight.price}")
        else:
            print("Flight not found.")
    elif len(user_input) == 3 and user_input.isalpha():
        source_flights = flight_table.search_by_source(user_input)
        if source_flights:
            for flight in source_flights:
                print(f"Flight ID: {flight.flight_id}, Source: {flight.source}, Destination: {flight.destination}, Price: {flight.price}")
        else:
            print("No flights found for the given source city.")
    elif len(user_input) == 3 and user_input.isalpha():
        destination_flights = flight_table.search_by_destination(user_input)
        if destination_flights:
            for flight in destination_flights:
                print(f"Flight ID: {flight.flight_id}, Source: {flight.source}, Destination: {flight.destination}, Price: {flight.price}")
        else:
            print("No flights found for the given destination city.")
    else:
        print("Invalid input.")

if __name__ == "__main__":
    main()
