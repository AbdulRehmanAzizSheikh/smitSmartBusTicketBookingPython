"""
Smart Bus Ticket Booking & Reservation System
=============================================

A beginner-friendly console application for a small bus service.
It manages routes, seat availability, bookings, cancellations and reports
using only Python's built-in data structures.

Storage note: all routes and bookings live in memory and are lost when the
program exits. Persistence is intentionally out of scope.

Run with:  python main.py
"""

SUPPORTED_CITIES = (
    "Karachi",
    "Hyderabad",
    "Sukkur",
    "Mirpur Khas",
    "Lahore",
)

ROUTES = [
    {
        "route_id": "R101",
        "departure_city": "Karachi",
        "destination_city": "Hyderabad",
        "departure_time": "08:00 AM",
        "ticket_price": 1200,
        "total_seats": 40,
        "available_seats": 40,
    },
    {
        "route_id": "R102",
        "departure_city": "Karachi",
        "destination_city": "Sukkur",
        "departure_time": "09:30 AM",
        "ticket_price": 2000,
        "total_seats": 36,
        "available_seats": 36,
    },
    {
        "route_id": "R103",
        "departure_city": "Hyderabad",
        "destination_city": "Mirpur Khas",
        "departure_time": "11:00 AM",
        "ticket_price": 800,
        "total_seats": 32,
        "available_seats": 32,
    },
    {
        "route_id": "R104",
        "departure_city": "Karachi",
        "destination_city": "Lahore",
        "departure_time": "07:00 PM",
        "ticket_price": 5000,
        "total_seats": 45,
        "available_seats": 45,
    },
    {
        "route_id": "R105",
        "departure_city": "Sukkur",
        "destination_city": "Hyderabad",
        "departure_time": "02:00 PM",
        "ticket_price": 1500,
        "total_seats": 30,
        "available_seats": 30,
    },
]

BOOKINGS = []
BOOKING_IDS = set()
NEXT_BOOKING_NUMBER = 1001


def find_route(route_id):
    """Return the route dictionary with the given route ID, or None."""
    for route in ROUTES:
        if route["route_id"].lower() == route_id.lower():
            return route
    return None


def find_booking(booking_id):
    """Return the booking dictionary with the given booking ID, or None."""
    for booking in BOOKINGS:
        if booking["booking_id"].lower() == booking_id.lower():
            return booking
    return None


def seat_status(available_seats, total_seats):
    """Classify how full a route is."""
    if available_seats <= 0:
        return "Fully Booked"
    if available_seats < total_seats:
        return "Partially Booked"
    return "Available"


def display_menu():
    """Print the main menu."""
    print()
    print("SMART BUS RESERVATION SYSTEM")
    print("===============================")
    print("1. View Available Routes")
    print("2. Search for a Route")
    print("3. Book a Ticket")
    print("4. View My Bookings")
    print("5. Cancel a Booking")
    print("6. View Seat Availability")
    print("7. Generate Booking Report")
    print("8. Exit")
    print("===============================")
    print("Enter your choice: ")


def view_available_routes():
    """List every route with its journey, fare and seat status."""
    print()
    print("AVAILABLE BUS ROUTES")
    print("No. Route Journey                  Depart      Fare        Seats   Status")
    print("-" * 105)
    for number, route in enumerate(ROUTES, start=1):
        status = seat_status(route["available_seats"], route["total_seats"])
        print(
            f"{number}.  {route['route_id']}  {route['departure_city']} -> "
            f"{route['destination_city']}  {route['departure_time']}  "
            f"Rs. {route['ticket_price']}  "
            f"{route['available_seats']}/{route['total_seats']}  {status}"
        )


def print_route_match(route):
    """Print a single route match during a search."""
    print(
        f"{route['route_id']} | {route['departure_city']} -> "
        f"{route['destination_city']} | Rs. {route['ticket_price']} | "
        f"{route['available_seats']} seats available"
    )


def search_route():
    """Search by route ID or by city (departure or destination)."""
    term = input("Search by route ID or city: ").strip()
    term_lower = term.lower()

    # First look for an exact route ID match; break stops the loop on hit.
    for route in ROUTES:
        if route["route_id"].lower() == term_lower:
            print_route_match(route)
            break
    # for-else: runs only when no route ID matched (loop completed without break)
    else:
        city_matches = [
            route
            for route in ROUTES
            if route["departure_city"].lower() == term_lower
            or route["destination_city"].lower() == term_lower
        ]
        if not city_matches:
            print(f"No routes found for '{term}'.")
        for route in city_matches:
            print_route_match(route)


def generate_booking_id():
    """Create a booking ID that is not used yet."""
    global NEXT_BOOKING_NUMBER
    booking_id = f"B{NEXT_BOOKING_NUMBER}"
    NEXT_BOOKING_NUMBER += 1
    BOOKING_IDS.add(booking_id)
    return booking_id


def book_ticket():
    """Collect passenger details, validate, confirm and update seats."""
    print()
    print("--- Book a Ticket ---")
    name = input("Enter passenger name: ").strip()
    if not name:
        print("Passenger name is required. Booking not created.")
        return

    age_input = input("Enter passenger age: ").strip()
    try:
        age = int(age_input)
    except ValueError:
        print("Age must be a positive integer. Booking not created.")
        return
    if age <= 0:
        print("Age must be a positive integer. Booking not created.")
        return

    route_id = input("Enter route ID: ").strip().upper()
    route = find_route(route_id)
    if route is None:
        print(f"No route found with ID {route_id}. Booking not created.")
        return

    seats_input = input("Enter number of seats: ").strip()
    try:
        seats = int(seats_input)
    except ValueError:
        print("Seat quantity must be a positive integer. Booking not created.")
        return
    if seats <= 0:
        print("Seat quantity must be a positive integer. Booking not created.")
        return

    if seats > route["available_seats"]:
        print(
            f"Only {route['available_seats']} seats available on {route['route_id']}. "
            "Booking not created."
        )
        return

    total_fare = route["ticket_price"] * seats
    booking_id = generate_booking_id()
    booking = {
        "booking_id": booking_id,
        "passenger_name": name,
        "passenger_age": age,
        "route_id": route["route_id"],
        "seats": seats,
        "total_fare": total_fare,
        "status": "Confirmed",
    }
    BOOKINGS.append(booking)
    route["available_seats"] -= seats

    print("Booking confirmed!")
    print(f"Booking ID: {booking_id}")
    print(f"Passenger: {name}")
    print(f"Route: {route['route_id']} ({route['departure_city']} -> {route['destination_city']})")
    print(f"Seats booked: {seats}")
    print(f"Fare per seat: Rs. {route['ticket_price']}")
    print(f"Total fare: Rs. {total_fare}")
    print(f"Status: {booking['status']}")


def view_my_bookings():
    """List all booking records, including cancelled ones."""
    print()
    print("MY BOOKINGS")
    if not BOOKINGS:
        print("No bookings found.")
        return
    for number, booking in enumerate(BOOKINGS, start=1):
        route = find_route(booking["route_id"])
        journey = (
            f"{route['departure_city']} -> {route['destination_city']}"
            if route
            else booking["route_id"]
        )
        print(
            f"{number}. Booking ID: {booking['booking_id']} | Passenger: "
            f"{booking['passenger_name']} | Route: {booking['route_id']} "
            f"({journey}) | Seats: {booking['seats']} | Fare: Rs. "
            f"{booking['total_fare']} | Status: {booking['status']}"
        )


def cancel_booking():
    """Cancel a Confirmed booking and restore its seats once."""
    booking_id = input("Enter booking ID to cancel: ").strip().upper()
    booking = find_booking(booking_id)
    if booking is None:
        print(f"Booking {booking_id} not found.")
        return
    if booking["status"] == "Cancelled":
        print(f"Booking {booking_id} is already cancelled.")
        return

    route = find_route(booking["route_id"])
    route["available_seats"] += booking["seats"]
    booking["status"] = "Cancelled"

    print(f"Booking {booking_id} has been cancelled.")
    print(f"Seats restored: {booking['seats']}")
    print(f"Route {booking['route_id']} available seats: {route['available_seats']}")


def view_seat_availability():
    """Show available seats vs total capacity and offer a filter."""
    print()
    print("SEAT AVAILABILITY")
    show_available_only = (
        input("Show only routes with seats available? (y/n): ").strip().lower()
        in ("y", "yes")
    )
    for route in ROUTES:
        status = seat_status(route["available_seats"], route["total_seats"])
        if show_available_only and status == "Fully Booked":
            continue
        print(
            f"{route['route_id']} | {route['departure_city']} -> "
            f"{route['destination_city']} | Available seats: "
            f"{route['available_seats']}/{route['total_seats']} | {status}"
        )


def generate_report():
    """Generate booking counts, reserved seats and confirmed revenue."""
    confirmed_bookings = [b for b in BOOKINGS if b["status"] == "Confirmed"]
    cancelled_bookings = [b for b in BOOKINGS if b["status"] == "Cancelled"]
    confirmed_revenue = sum(b["total_fare"] for b in confirmed_bookings)
    reserved_seats = sum(b["seats"] for b in confirmed_bookings)
    fully_booked_routes = sum(1 for r in ROUTES if r["available_seats"] == 0)

    print()
    print("BOOKING REPORT")
    print(f"Total bookings created: {len(BOOKINGS)}")
    print(f"Confirmed bookings: {len(confirmed_bookings)}")
    print(f"Cancelled bookings: {len(cancelled_bookings)}")
    print(f"Seats currently reserved: {reserved_seats}")
    print(f"Confirmed revenue: Rs. {confirmed_revenue:,}")
    print(f"Fully booked routes: {fully_booked_routes}")


def show_schedule():
    """Print routes grouped by departure city."""
    print()
    print("ROUTE SCHEDULE BY DEPARTURE CITY")
    for city in SUPPORTED_CITIES:
        print(f"{city}")
        city_has_departure = False
        for route in ROUTES:
            if route["departure_city"] == city:
                city_has_departure = True
                print(f"  {route['route_id']} -> {route['destination_city']} | {route['departure_time']}")
        if not city_has_departure:
            print("  No scheduled departures.")


def main():
    print("Welcome to the Smart Bus Reservation System!")
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            view_available_routes()
        elif choice == "2":
            search_route()
        elif choice == "3":
            book_ticket()
        elif choice == "4":
            view_my_bookings()
        elif choice == "5":
            cancel_booking()
        elif choice == "6":
            view_seat_availability()
        elif choice == "7":
            generate_report()
            show_schedule()
        elif choice == "8":
            print("Thank you for using the Smart Bus Reservation System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")
            continue


if __name__ == "__main__":
    main()
