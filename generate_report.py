from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Table,
    TableStyle,
    Image
)
import os


# ============================================================
# FILE SETTINGS
# ============================================================

PROJECT_FOLDER = os.path.dirname(os.path.abspath(__file__))
DOCS_FOLDER = os.path.join(PROJECT_FOLDER, "docs")

OUTPUT_FILE = os.path.join(
    PROJECT_FOLDER,
    "Hotel_Booking_Management_System_Final_Report.pdf"
)


# ============================================================
# STYLES
# ============================================================

styles = getSampleStyleSheet()

styles.add(
    ParagraphStyle(
        name="CoverTitle",
        parent=styles["Title"],
        fontSize=24,
        leading=30,
        alignment=TA_CENTER,
        spaceAfter=20
    )
)

styles.add(
    ParagraphStyle(
        name="CoverSubtitle",
        parent=styles["Normal"],
        fontSize=14,
        leading=20,
        alignment=TA_CENTER,
        spaceAfter=10
    )
)

styles.add(
    ParagraphStyle(
        name="SectionTitle",
        parent=styles["Heading1"],
        fontSize=18,
        leading=23,
        spaceBefore=8,
        spaceAfter=12
    )
)

styles.add(
    ParagraphStyle(
        name="SubTitle",
        parent=styles["Heading2"],
        fontSize=13,
        leading=17,
        spaceBefore=8,
        spaceAfter=6
    )
)

styles.add(
    ParagraphStyle(
        name="BodyCustom",
        parent=styles["BodyText"],
        fontSize=9.5,
        leading=14,
        spaceAfter=7
    )
)

styles.add(
    ParagraphStyle(
        name="SmallCenter",
        parent=styles["BodyText"],
        fontSize=8,
        leading=11,
        alignment=TA_CENTER
    )
)


def paragraph(text):
    return Paragraph(text, styles["BodyCustom"])


def bullet(text):
    return Paragraph(
        "• " + text,
        styles["BodyCustom"]
    )


# ============================================================
# TABLE FUNCTION
# ============================================================

def make_table(data, widths):
    table = Table(
        data,
        colWidths=widths,
        repeatRows=1
    )

    table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E8EEF5")),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )

    return table


# ============================================================
# DIAGRAM PATHS
# ============================================================

architecture_image = os.path.join(
    DOCS_FOLDER,
    "system_architecture.png"
)

use_case_image = os.path.join(
    DOCS_FOLDER,
    "use_case_diagram.png"
)

workflow_image = os.path.join(
    DOCS_FOLDER,
    "workflow_diagram.png"
)


# ============================================================
# PDF DOCUMENT
# ============================================================

document = SimpleDocTemplate(
    OUTPUT_FILE,
    pagesize=A4,
    rightMargin=1.7 * cm,
    leftMargin=1.7 * cm,
    topMargin=1.7 * cm,
    bottomMargin=1.8 * cm,
    title="Hotel Booking Management System",
    author="Python Essentials / FlipCourse Project"
)

story = []


# ============================================================
# COVER PAGE
# ============================================================

story.append(Spacer(1, 3 * cm))

story.append(
    Paragraph(
        "HOTEL BOOKING MANAGEMENT SYSTEM",
        styles["CoverTitle"]
    )
)

story.append(
    Paragraph(
        "Python Command-Line Application",
        styles["CoverSubtitle"]
    )
)

story.append(Spacer(1, 1 * cm))

story.append(
    Paragraph(
        "<b>PROJECT REPORT</b>",
        styles["CoverSubtitle"]
    )
)

story.append(Spacer(1, 1 * cm))

story.append(
    Paragraph(
        "Developed as part of the Python Essentials / FlipCourse Project",
        styles["CoverSubtitle"]
    )
)

story.append(Spacer(1, 1 * cm))

story.append(
    Paragraph(
        "<b>Technology:</b> Python 3",
        styles["CoverSubtitle"]
    )
)

story.append(
    Paragraph(
        "<b>Application Type:</b> Command-Line Interface",
        styles["CoverSubtitle"]
    )
)

story.append(
    Paragraph(
        "<b>Data Storage:</b> CSV Files",
        styles["CoverSubtitle"]
    )
)

story.append(Spacer(1, 2 * cm))

story.append(
    Paragraph(
        "Final Project Submission Report",
        styles["CoverSubtitle"]
    )
)

story.append(PageBreak())


# ============================================================
# 1. INTRODUCTION
# ============================================================

story.append(
    Paragraph("1. Introduction", styles["SectionTitle"])
)

story.append(
    paragraph(
        "The Hotel Booking Management System is a modular command-line "
        "Python application designed to support the basic operations of "
        "a small hotel. The system combines room management, customer "
        "management, booking management, cancellation, billing, and "
        "reporting into one application."
    )
)

story.append(
    paragraph(
        "The project demonstrates foundational Python programming "
        "concepts including functions, modules, conditional statements, "
        "loops, input validation, file handling, CSV processing, and "
        "modular program design."
    )
)

story.append(
    paragraph(
        "Persistent information is maintained using CSV files so that "
        "room, customer, and booking information remains available "
        "after the application is closed."
    )
)


# ============================================================
# 2. PROBLEM STATEMENT
# ============================================================

story.append(
    Paragraph("2. Problem Statement", styles["SectionTitle"])
)

story.append(
    paragraph(
        "Managing hotel rooms, customer information, bookings, and "
        "billing manually can be time-consuming and may lead to "
        "errors. A simple computerized system can organize these "
        "activities and provide a consistent workflow for hotel staff."
    )
)

story.append(
    paragraph(
        "The proposed system provides a centralized command-line "
        "solution for maintaining hotel room records, customer records, "
        "booking records, billing calculations, and basic operational "
        "reports."
    )
)


# ============================================================
# 3. OBJECTIVES
# ============================================================

story.append(
    Paragraph("3. Objectives", styles["SectionTitle"])
)

objectives = [
    "Develop a functional hotel booking management application using Python.",
    "Provide separate modules for room, customer, booking, billing, reporting, validation, and storage operations.",
    "Allow hotel staff to perform basic CRUD operations on room and customer records.",
    "Prevent invalid booking operations such as booking an occupied or nonexistent room.",
    "Automatically calculate bills using room price and number of nights.",
    "Maintain persistent data using CSV files.",
    "Demonstrate modular programming and maintainable project organization.",
    "Use Git and GitHub for version control and project delivery."
]

for item in objectives:
    story.append(bullet(item))


# ============================================================
# 4. SCOPE
# ============================================================

story.append(
    Paragraph("4. Scope of the Project", styles["SectionTitle"])
)

scope_items = [
    "Room viewing, addition, updating, and deletion of available rooms.",
    "Customer addition, viewing, updating, and deletion.",
    "Booking creation, viewing, and cancellation.",
    "Automatic room-status updates during booking and cancellation.",
    "Bill generation for active bookings.",
    "Hotel summary and available-room reports.",
    "CSV-based local data persistence.",
    "Command-line interaction."
]

for item in scope_items:
    story.append(bullet(item))

story.append(
    paragraph(
        "<b>Out of scope:</b> online payments, customer login, "
        "online reservation portals, real-time multi-user synchronization, "
        "and external database servers."
    )
)


# ============================================================
# 5. FUNCTIONAL REQUIREMENTS
# ============================================================

story.append(
    Paragraph("5. Functional Requirements", styles["SectionTitle"])
)

functional_data = [
    ["Module", "Functional Requirements"],

    [
        "Room Management",
        "View rooms; add rooms; update room details; "
        "delete available rooms; track room status."
    ],

    [
        "Customer Management",
        "Add, view, update, and delete customer records."
    ],

    [
        "Booking Management",
        "Create bookings; verify customer; verify room; "
        "check availability; view bookings; cancel bookings."
    ],

    [
        "Billing",
        "Generate a bill for an active booking using "
        "room price and number of nights."
    ],

    [
        "Reports",
        "Display total rooms, available rooms, occupied rooms, "
        "customers, active bookings, cancelled bookings, "
        "and available rooms."
    ]
]

story.append(
    make_table(
        functional_data,
        [4.2 * cm, 11.8 * cm]
    )
)


# ============================================================
# 6. NON-FUNCTIONAL REQUIREMENTS
# ============================================================

story.append(
    Paragraph(
        "6. Non-Functional Requirements",
        styles["SectionTitle"]
    )
)

nonfunctional_data = [
    ["Requirement", "Description"],

    [
        "Usability",
        "The system should be simple and easy to operate "
        "through a menu-driven command-line interface."
    ],

    [
        "Reliability",
        "The system validates user input and prevents invalid "
        "operations such as booking an occupied room."
    ],

    [
        "Maintainability",
        "The application is divided into separate Python modules "
        "for different functionalities."
    ],

    [
        "Data Persistence",
        "Room, customer, and booking information remains stored "
        "in CSV files after the application is closed."
    ],

    [
        "Performance",
        "Basic operations should execute quickly for a small "
        "hotel dataset."
    ],

    [
        "Error Handling",
        "The system displays meaningful messages when invalid "
        "input or unavailable records are entered."
    ]
]

story.append(
    make_table(
        nonfunctional_data,
        [4.2 * cm, 11.8 * cm]
    )
)


# ============================================================
# 7. TARGET USERS
# ============================================================

story.append(
    Paragraph("7. Target Users", styles["SectionTitle"])
)

for item in [
    "Hotel reception staff",
    "Small hotel administrators",
    "Hotel booking operators"
]:
    story.append(bullet(item))


# ============================================================
# 8. TECHNOLOGY STACK
# ============================================================

story.append(
    Paragraph("8. Technology Stack", styles["SectionTitle"])
)

technology_data = [
    ["Technology / Tool", "Purpose"],

    ["Python 3", "Application development"],

    ["CSV Module", "Reading and writing persistent CSV data"],

    ["Command Line Interface", "User interaction"],

    ["Git", "Version control"],

    ["GitHub", "Remote repository and project hosting"]
]

story.append(
    make_table(
        technology_data,
        [5 * cm, 11 * cm]
    )
)

story.append(PageBreak())


# ============================================================
# 9. SYSTEM ARCHITECTURE
# ============================================================

story.append(
    Paragraph("9. System Architecture", styles["SectionTitle"])
)

story.append(
    paragraph(
        "The system follows a modular architecture. The command-line "
        "interface is controlled by main.py, which routes user choices "
        "to specialized modules."
    )
)

story.append(
    paragraph(
        "Validation is handled by validation.py, while CSV file "
        "operations are handled by storage.py. The main functional "
        "modules are room_manager.py, customer_manager.py, "
        "booking_manager.py, billing.py, and reports.py."
    )
)

if os.path.exists(architecture_image):
    story.append(
        Image(
            architecture_image,
            width=16 * cm,
            height=8.8 * cm
        )
    )

    story.append(
        Paragraph(
            "Figure 1. System Architecture",
            styles["SmallCenter"]
        )
    )


# ============================================================
# 10. PROJECT STRUCTURE
# ============================================================

story.append(
    Paragraph("10. Project Structure", styles["SectionTitle"])
)

structure_data = [
    ["Path", "Purpose"],

    ["src/main.py", "Main menu and application control"],

    ["src/room_manager.py", "Room operations"],

    ["src/customer_manager.py", "Customer operations"],

    ["src/booking_manager.py", "Booking and cancellation operations"],

    ["src/billing.py", "Bill calculation and display"],

    ["src/reports.py", "Hotel reports"],

    ["src/validation.py", "Input validation"],

    ["src/storage.py", "CSV reading and writing"],

    ["data/*.csv", "Persistent room, customer, and booking records"],

    ["tests/", "Automated validation tests"],

    ["docs/", "Requirements, design documentation, and diagrams"]
]

story.append(
    make_table(
        structure_data,
        [5 * cm, 11 * cm]
    )
)

story.append(PageBreak())


# ============================================================
# 11. USE CASE DESIGN
# ============================================================

story.append(
    Paragraph("11. Use Case Design", styles["SectionTitle"])
)

story.append(
    paragraph(
        "The primary actor is the Hotel Staff member. The staff "
        "interacts with the command-line system to manage rooms and "
        "customers, create or cancel bookings, generate bills, "
        "and view reports."
    )
)

if os.path.exists(use_case_image):
    story.append(
        Image(
            use_case_image,
            width=16 * cm,
            height=8.8 * cm
        )
    )

    story.append(
        Paragraph(
            "Figure 2. Use Case Diagram",
            styles["SmallCenter"]
        )
    )


# ============================================================
# 12. SYSTEM WORKFLOW
# ============================================================

story.append(
    Paragraph("12. System Workflow", styles["SectionTitle"])
)

story.append(
    paragraph(
        "A typical booking workflow begins when hotel staff selects "
        "Booking Management. The system verifies the customer, "
        "verifies the room, checks room availability, records the "
        "booking, updates the room status, and allows billing and "
        "reporting operations."
    )
)

if os.path.exists(workflow_image):
    story.append(
        Image(
            workflow_image,
            width=16 * cm,
            height=8.8 * cm
        )
    )

    story.append(
        Paragraph(
            "Figure 3. System Workflow",
            styles["SmallCenter"]
        )
    )


# ============================================================
# 13. CLASS / COMPONENT DESIGN
# ============================================================

story.append(
    Paragraph(
        "13. Class / Component Design",
        styles["SectionTitle"]
    )
)

story.append(
    paragraph(
        "The application is organized into separate Python components. "
        "main.py controls the application flow, while room_manager.py, "
        "customer_manager.py, and booking_manager.py implement the "
        "main operational modules. billing.py and reports.py provide "
        "supporting business functions."
    )
)

component_data = [
    ["Component", "Responsibility"],

    ["main.py", "Main menu and application control"],

    ["room_manager.py", "Room management"],

    ["customer_manager.py", "Customer management"],

    ["booking_manager.py", "Booking and cancellation"],

    ["billing.py", "Bill generation"],

    ["reports.py", "Hotel reports"],

    ["validation.py", "Input validation"],

    ["storage.py", "CSV data storage"]
]

story.append(
    make_table(
        component_data,
        [5 * cm, 11 * cm]
    )
)


# ============================================================
# 14. SEQUENCE DESIGN
# ============================================================

story.append(
    Paragraph(
        "14. Sequence Design",
        styles["SectionTitle"]
    )
)

sequence_steps = [
    "The user selects Booking Management from the main menu.",
    "main.py calls the booking management function.",
    "booking_manager.py requests the customer ID.",
    "The system checks customer information using storage.py.",
    "The user enters the room number.",
    "The system checks room information and availability.",
    "The user enters the number of nights.",
    "The booking is stored in bookings.csv.",
    "The room status is changed to Occupied.",
    "The updated room information is stored in rooms.csv.",
    "The system displays a successful booking message."
]

for i, item in enumerate(sequence_steps, 1):
    story.append(
        paragraph(
            f"<b>{i}.</b> {item}"
        )
    )


# ============================================================
# 15. DATA STORAGE / ER DESIGN
# ============================================================

story.append(
    Paragraph(
        "15. Data Storage and ER Design",
        styles["SectionTitle"]
    )
)

story.append(
    paragraph(
        "The system uses three CSV files for persistent storage. "
        "Customer and room identifiers are referenced by booking "
        "records to connect related information."
    )
)

storage_data = [
    ["File", "Fields"],

    [
        "rooms.csv",
        "room_number, room_type, price, status"
    ],

    [
        "customers.csv",
        "customer_id, name, phone, email"
    ],

    [
        "bookings.csv",
        "booking_id, customer_id, room_number, "
        "number_of_nights, status"
    ]
]

story.append(
    make_table(
        storage_data,
        [5 * cm, 11 * cm]
    )
)

story.append(
    paragraph(
        "<b>Relationships:</b> One customer can have multiple bookings. "
        "Each booking is associated with one customer and one room. "
        "Room status is updated when a booking is created or cancelled."
    )
)

story.append(PageBreak())


# ============================================================
# 16. DESIGN DECISIONS
# ============================================================

story.append(
    Paragraph(
        "16. Design Decisions and Rationale",
        styles["SectionTitle"]
    )
)

design_data = [
    ["Decision", "Rationale"],

    [
        "Modular Python files",
        "Separates responsibilities and makes the project easier "
        "to understand and maintain."
    ],

    [
        "CSV storage",
        "Simple, lightweight, human-readable storage suitable "
        "for a small academic CLI application."
    ],

    [
        "Central validation module",
        "Avoids repeating common input-validation logic."
    ],

    [
        "Menu-driven CLI",
        "Provides a straightforward interface using core Python concepts."
    ],

    [
        "Room status tracking",
        "Prevents double booking and releases rooms after cancellation."
    ]
]

story.append(
    make_table(
        design_data,
        [5 * cm, 11 * cm]
    )
)


# ============================================================
# 17. IMPLEMENTATION DETAILS
# ============================================================

story.append(
    Paragraph(
        "17. Implementation Details",
        styles["SectionTitle"]
    )
)

story.append(
    paragraph(
        "<b>Room Management:</b> The system reads rooms from rooms.csv "
        "and supports viewing, adding, updating, and deleting rooms. "
        "Occupied rooms cannot be deleted."
    )
)

story.append(
    paragraph(
        "<b>Customer Management:</b> Customer records are stored in "
        "customers.csv. Customer IDs are checked for duplicates before "
        "a new customer is added."
    )
)

story.append(
    paragraph(
        "<b>Booking Management:</b> A booking can only be created when "
        "the customer exists and the selected room exists and is available. "
        "A successful booking changes the room status to Occupied."
    )
)

story.append(
    paragraph(
        "<b>Cancellation:</b> Cancelling an active booking changes its "
        "status to Cancelled and changes the related room status back "
        "to Available."
    )
)

story.append(
    paragraph(
        "<b>Billing:</b> The total amount is calculated by multiplying "
        "the room price per night by the number of nights."
    )
)

story.append(
    paragraph(
        "<b>Reports:</b> The reports module counts rooms, customers, "
        "and bookings and provides a list of currently available rooms."
    )
)

story.append(
    paragraph(
        "<b>Validation:</b> validation.py handles non-empty input, "
        "positive numbers, and positive integers."
    )
)


# ============================================================
# 18. TESTING
# ============================================================

story.append(
    Paragraph(
        "18. Testing Approach",
        styles["SectionTitle"]
    )
)

story.append(
    paragraph(
        "The project uses both manual application testing and "
        "automated unit testing for the validation module. "
        "The automated tests use Python's built-in unittest framework."
    )
)

testing_data = [
    ["Test Case", "Expected Result", "Result"],

    [
        "Launch application",
        "Main menu displayed",
        "Passed"
    ],

    [
        "View rooms",
        "Room list displayed",
        "Passed"
    ],

    [
        "Add customer",
        "Customer record saved",
        "Passed"
    ],

    [
        "Create booking",
        "Booking created and room becomes Occupied",
        "Passed"
    ],

    [
        "Generate bill",
        "Correct total calculated",
        "Passed"
    ],

    [
        "Hotel summary",
        "Hotel statistics displayed",
        "Passed"
    ],

    [
        "Cancel booking",
        "Booking cancelled and room becomes Available",
        "Passed"
    ],

    [
        "Invalid numeric input",
        "Validation message displayed",
        "Implemented"
    ],

    [
        "Book occupied room",
        "Booking rejected",
        "Implemented"
    ]
]

story.append(
    make_table(
        testing_data,
        [5 * cm, 7 * cm, 4 * cm]
    )
)

story.append(
    paragraph(
        "<b>Automated validation testing:</b> 3 tests were executed "
        "using unittest and all 3 tests passed successfully."
    )
)

story.append(
    paragraph(
        "The three automated tests cover non-empty input, positive "
        "number input, and positive integer input."
    )
)

story.append(
    paragraph(
        "A representative manual test used customer ID C001, room 101, "
        "and two nights. Room 101 costs ₹1500 per night, resulting in "
        "a calculated bill of ₹3000."
    )
)


# ============================================================
# 19. RESULTS
# ============================================================

story.append(
    Paragraph(
        "19. Results",
        styles["SectionTitle"]
    )
)

results = [
    "The application successfully launches from the command line.",
    "Room records can be viewed and maintained.",
    "Customer records can be added and maintained.",
    "Bookings update room occupancy status.",
    "Cancelled bookings release the associated room.",
    "Billing calculates the total from room price and number of nights.",
    "Reports summarize current hotel data.",
    "CSV files provide persistent local storage.",
    "Automated validation tests execute successfully."
]

for item in results:
    story.append(bullet(item))


# ============================================================
# 20. CHALLENGES
# ============================================================

story.append(
    Paragraph(
        "20. Challenges",
        styles["SectionTitle"]
    )
)

challenges = [
    "Designing separate modules while keeping the application workflow simple.",
    "Keeping room and booking statuses synchronized across CSV files.",
    "Handling invalid input without terminating the program.",
    "Maintaining consistent field names across multiple CSV files.",
    "Organizing source code, documentation, diagrams, tests, and GitHub files."
]

for item in challenges:
    story.append(bullet(item))


# ============================================================
# 21. LEARNINGS
# ============================================================

story.append(
    Paragraph(
        "21. Learnings",
        styles["SectionTitle"]
    )
)

learnings = [
    "Practical use of Python modules and functions.",
    "Reading and writing structured data using CSV files.",
    "Using loops and conditions to implement application logic.",
    "Implementing validation and error handling.",
    "Designing a modular command-line application.",
    "Using unittest for automated testing.",
    "Using Git for version control and GitHub for project hosting.",
    "Preparing technical documentation and software design diagrams."
]

for item in learnings:
    story.append(bullet(item))


# ============================================================
# 22. FUTURE ENHANCEMENTS
# ============================================================

story.append(
    Paragraph(
        "22. Future Enhancements",
        styles["SectionTitle"]
    )
)

future = [
    "Replace CSV storage with SQLite or MySQL.",
    "Add check-in and check-out dates.",
    "Add customer search and filtering.",
    "Add automated invoice file generation.",
    "Add authentication and role-based access.",
    "Add a graphical or web-based user interface.",
    "Add more automated unit and integration tests.",
    "Add occupancy and revenue analytics."
]

for item in future:
    story.append(bullet(item))


# ============================================================
# 23. GITHUB / VERSION CONTROL
# ============================================================

story.append(
    Paragraph(
        "23. GitHub and Version Control",
        styles["SectionTitle"]
    )
)

story.append(
    paragraph(
        "The project is maintained in a Git repository with the main "
        "branch hosted on GitHub. The repository contains the source "
        "code, CSV data files, documentation, diagrams, README.md, "
        "statement.md, requirements.txt, tests, and project configuration."
    )
)

story.append(
    paragraph(
        "<b>GitHub Repository:</b> "
        "github.com/PRANJALBHATI/Hotel-Booking-Management-System"
    )
)

story.append(
    paragraph(
        "Git commits were used to track the initial implementation, "
        "generated-file cleanup, documentation, design diagrams, and "
        "automated testing updates."
    )
)


# ============================================================
# 24. CONCLUSION
# ============================================================

story.append(
    Paragraph(
        "24. Conclusion",
        styles["SectionTitle"]
    )
)

story.append(
    paragraph(
        "The Hotel Booking Management System provides a complete "
        "small-scale hotel management workflow using Python and CSV "
        "storage. It demonstrates core programming concepts together "
        "with modular software design, input validation, persistent "
        "data handling, documentation, testing, and Git-based version control."
    )
)

story.append(
    paragraph(
        "The project provides a foundation that can be extended with "
        "database storage, dates, authentication, automated testing, "
        "and a graphical or web interface in future versions."
    )
)


# ============================================================
# 25. REFERENCES
# ============================================================

story.append(
    Paragraph(
        "25. References",
        styles["SectionTitle"]
    )
)

references = [
    "Python 3 Standard Library documentation and Python programming concepts.",
    "Git documentation and GitHub version-control workflow.",
    "Python Essentials / FlipCourse project requirements and specifications.",
    "Project source code and documentation contained in the Hotel Booking Management System repository."
]

for item in references:
    story.append(bullet(item))


# ============================================================
# PAGE FOOTER
# ============================================================

def add_footer(canvas, doc):
    canvas.saveState()

    canvas.setFont("Helvetica", 8)

    canvas.drawString(
        1.7 * cm,
        1.1 * cm,
        "Hotel Booking Management System - Project Report"
    )

    canvas.drawRightString(
        A4[0] - 1.7 * cm,
        1.1 * cm,
        "Page " + str(doc.page)
    )

    canvas.restoreState()


# ============================================================
# BUILD PDF
# ============================================================

document.build(
    story,
    onFirstPage=add_footer,
    onLaterPages=add_footer
)

print()
print("==============================================")
print("PDF GENERATED SUCCESSFULLY")
print("==============================================")
print()
print("File:")
print(OUTPUT_FILE)
print()
print("The report contains:")
print("- Cover Page")
print("- Introduction")
print("- Problem Statement")
print("- Objectives")
print("- Scope")
print("- Functional Requirements")
print("- Non-Functional Requirements")
print("- Target Users")
print("- Technology Stack")
print("- System Architecture")
print("- Project Structure")
print("- Use Case Design")
print("- Workflow")
print("- Class / Component Design")
print("- Sequence Design")
print("- Data Storage / ER Design")
print("- Design Decisions")
print("- Implementation Details")
print("- Testing")
print("- Automated Test Results")
print("- Results")
print("- Challenges")
print("- Learnings")
print("- Future Enhancements")
print("- GitHub / Version Control")
print("- Conclusion")
print("- References")
print()
print("==============================================")