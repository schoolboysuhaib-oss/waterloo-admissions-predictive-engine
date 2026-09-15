# Waterloo CS Academic Predictive Algorithmic Engine (V1.2.0)

An interactive computational software tool engineered in Python to evaluate secondary academic profiles and calculate empirical admission success margins using statistical Monte Carlo modeling.

## 🧮 Core Architecture & Logic
* **Object-Oriented Academic Profiling:** Structured dedicated software classes (`HighSchoolCourse`, `AcademicProfile`) to securely handle state tracking for prerequisite configurations and custom elective arrays.
* **Admission Policy Enforcement:** Implemented programmatic filters replicating Waterloo's strict multi-attempt repetition constraints, applying automatic 5.0% point deductions to target course matrices.
* **10,000-Iteration Monte Carlo Engine:** Integrated random Gaussian noise distributions to simulate real-world academic score variance across incomplete semesters, executing 10,000 parallel test matrices per run.
* **Dynamic CLI Execution Loop:** Engineered a persistent command-line interaction block to handle real-time parameter changes without altering source configurations.
