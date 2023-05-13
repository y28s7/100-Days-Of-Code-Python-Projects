class FlightData:

    def __init__(self, from_airport, from_city, to_airport, to_city, nights_in_dest, price, out_date, return_date,
                 via_city="", stopovers=0):
        self.price = price
        self.from_airport = from_airport
        self.from_city = from_city
        self.to_airport = to_airport
        self.to_city = to_city
        self.nights_in_dest = nights_in_dest
        self.out_date = out_date[0]
        self.return_date = return_date[0]
        self.via_city = via_city
        self.stopovers = stopovers
