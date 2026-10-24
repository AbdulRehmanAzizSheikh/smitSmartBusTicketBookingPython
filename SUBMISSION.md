# Smart Bus Ticket Booking & Reservation System

## Submission Text

### 1. Project Overview

The Smart Bus Ticket Booking & Reservation System is a beginner-friendly Python 3 console application
for a small bus service. It manages routes, seat availability, bookings, cancellations and reports
through a text-based menu.

The application delivers an end-to-end reservation workflow: valid requests create unique booking IDs,
seat counts stay correct, cancellations restore seats exactly once, and reports exclude cancelled
bookings from confirmed revenue.

### 2. Objective

To provide a small, understandable reservation system that models essential bus-ticket logic without
databases, external services or advanced frameworks.

### 3. Features Implemented

- Route storage and display of all available routes with seat status.
- Search by route ID or city (case-insensitive, departure or destination match).
- Ticket booking with full validation and fare calculation (fare = ticket price x seats).
- Booking ID generation with uniqueness.
- My bookings view, including cancelled records.
- Cancellation of Confirmed bookings only, with one-time seat restoration.
- Seat availability view with status and filter.
- Booking report with counts, reserved seats, confirmed revenue and fully booked routes.
- Route schedule grouped by departure city.

### 4. Technical Implementation

- Language: Python 3 (built-in functionality only, no external packages).
- Data structures: lists and dictionaries for routes/bookings, set for booking IDs, tuple for cities.
- Control flow: while loops, for loops, nested loops, for-else, break, continue, enumerate.
- Validation performed before any state change.

### 5. Business Rules Verified

BR-01 to BR-15 were implemented and tested, including blank-name rejection, positive-age validation,
unknown-route rejection, positive-seat enforcement, capacity checks, unique booking IDs, fare accuracy,
single seat restoration and confirmed-only revenue calculation.

### 6. Testing

All required tests TC-01 to TC-12 were executed against the application and all matched the expected
behavior.

### 7. Deliverables

- main.py - complete runnable source.
- README.md - purpose, run instructions, menu guide and constraints.
- test_cases.txt - scenario, input, expected, actual and matched status.
- Screenshots/demo - submission_smart_bus_1.png (menu + routes), submission_smart_bus_2.png (booking + report).

### 8. Conclusion

The final application demonstrates a working, tested bus-ticket reservation workflow using beginner-level
Python fundamentals, accurate availability, reliable cancellation and understandable reports.

---

**GitHub Repository:** https://github.com/AbdulRehmanAzizSheikh/smitSmartBusTicketBookingPython
**Run Command:** python main.py
