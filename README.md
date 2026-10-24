# Smart Bus Ticket Booking & Reservation System

A beginner-friendly console application for a small bus service that manages
routes, seat availability, bookings, cancellations and reports.

Built for the **Smart Bus Ticket Booking & Reservation System Product
Requirements Document (PRD)**.

---

## Purpose

The system lets a passenger or operator work through a console menu to:

- Browse bus routes and compare journeys.
- Search for a route by route ID or city.
- Book seats and receive a unique booking ID.
- Review booking history.
- Cancel a confirmed booking and restore seats.
- Check seat availability.
- Generate booking reports and view schedules.

The final product delivers an end-to-end reservation workflow: valid requests
create unique booking IDs, seat counts stay correct, cancellations restore
seats exactly once, and reports exclude cancelled bookings from confirmed
revenue.

---

## Python Requirement

- **Python 3** (3.8 or newer recommended).
- **No external libraries.** Only built-in Python functionality is used.

Run with:

```bash
python main.py
```

---

## Menu Guide

```
SMART BUS RESERVATION SYSTEM
===============================
1. View Available Routes
2. Search for a Route
3. Book a Ticket
4. View My Bookings
5. Cancel a Booking
6. View Seat Availability
7. Generate Booking Report
8. Exit
===============================
Enter your choice:
```

| Option | Behavior |
| --- | --- |
| 1 | List all routes with journey, departure time, fare and seats available. |
| 2 | Search by route ID or city (departure or destination). |
| 3 | Collect passenger details, validate, calculate fare, confirm and update seats. |
| 4 | List all bookings, including cancelled records. |
| 5 | Cancel only an existing Confirmed booking. |
| 6 | Show available seats vs total capacity; offers a filter. |
| 7 | Generate counts, reserved seats, revenue and fully-booked routes. |
| 8 | Exit the menu loop cleanly. |

Invalid or unsupported choices show a helpful message and return to the menu.

---

## Sample Workflow

1. Start the program and choose `1` to view routes.
2. Choose `2` and search a city such as `hyderabad`.
3. Choose `3` and book e.g. `Ahmed`, age `24`, route `R101`, seats `2`.
4. Booking `B1001` is confirmed and the fare is `Rs. 2400`.
5. Check availability or generate the report with `7`.
6. Cancel with `5` using booking ID `B1001` to restore seats.

---

## Storage Limitation

Route and booking records stay **in memory** while the program runs. They are
**not persisted** and are lost when the application closes. Persistence across
restarts is intentionally out of scope.

---

## Constraints

- Console text menu only (no GUI, website or mobile app).
- In-memory routes, passenger and booking records.
- No database, payment gateway, third-party API or external Python library.
- Built-in Python only.

---

## Optional Enhancements

Optional enhancements (10% discount for four or more seats, fare categories,
popular route, individual seat numbers, passenger search, revenue by city) are
not required for the core version and were not implemented.
