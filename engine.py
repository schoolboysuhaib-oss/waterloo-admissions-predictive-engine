"""
=============================================================================
PROJECT:  WATERLOO CS ACADEMIC PREDICTIVE ALGORITHMIC ENGINE (V1.2.0-INTERACTIVE)
TARGET:   Python 3.9+ Runtime Environment
PARADIGM: Object-Oriented Programming (OOP) & Dynamic Monte Carlo Simulation
=============================================================================
"""

import math
import random

class HighSchoolCourse:
    """Represents an individual Ontario Grade 12 academic credit (4U/4M)."""
    def __init__(self, code: str, grade: float, attempts: int = 1):
        self.code = code.upper().strip()
        self.grade = float(grade)
        self.attempts = int(attempts)
        
    def calculate_effective_grade(self, deduction_policy: float = 5.0) -> float:
        """Enforces Waterloo's strict 5% multi-attempt repetition deduction."""
        if self.attempts > 1:
            effective = self.grade - deduction_policy
            return max(0.0, effective)
        return self.grade

class AcademicProfile:
    """Manages prerequisites and electives to compile a top-6 admission average."""
    def __init__(self, student_name: str):
        self.student_name = student_name
        self.completed_courses = {}
        self.projected_courses = {}
        
    def add_completed_course(self, code: str, grade: float, attempts: int = 1):
        self.completed_courses[code.upper()] = HighSchoolCourse(code, grade, attempts)
        
    def add_projected_course(self, code: str, target_grade: float):
        self.projected_courses[code.upper()] = target_grade

    def compile_admission_average(self) -> float:
        processed_grades = []
        prereqs = ["MHF4U", "MCV4U", "ENG4U"]
        
        for req in prereqs:
            if req in self.completed_courses:
                course = self.completed_courses[req]
                processed_grades.append(course.calculate_effective_grade())
            elif req in self.projected_courses:
                processed_grades.append(self.projected_courses[req])
            else:
                processed_grades.append(0.0)
                
        electives = []
        for code, course in self.completed_courses.items():
            if code not in prereqs:
                electives.append(course.calculate_effective_grade())
        for code, grade in self.projected_courses.items():
            if code not in prereqs:
                electives.append(grade)
                
        electives.sort(reverse=True)
        needed_electives = 6 - len(processed_grades)
        processed_grades.extend(electives[:needed_electives])
        
        return sum(processed_grades) / len(processed_grades) if processed_grades else 0.0

def run_simulation(eng_target: float, hsc_target: float, bbb_target: float, boh_target: float, cutoff: float):
    sim_trials = 10000
    successful_admissions = 0
    
    for _ in range(sim_trials):
        trial_profile = AcademicProfile("Simulation Trial")
        trial_profile.add_completed_course("MHF4U", 94.0, attempts=3)
        trial_profile.add_completed_course("MCV4U", 86.0, attempts=1)
        
        # Inject standard academic variance noise (Gaussian distribution)
        trial_profile.add_projected_course("ENG4U", random.gauss(eng_target, 1.2))
        trial_profile.add_projected_course("HSC4M", random.gauss(hsc_target, 1.0))
        trial_profile.add_projected_course("BBB4M", random.gauss(bbb_target, 1.0))
        trial_profile.add_projected_course("BOH4M", random.gauss(boh_target, 1.0))
        
        if trial_profile.compile_admission_average() >= cutoff:
            successful_admissions += 1
            
    return (successful_admissions / sim_trials) * 100

if __name__ == "__main__":
    print("=====================================================================")
    print("SYSTEM ACTIVE: WATERLOO COMP-SCI ADMISSIONS PREDICTIVE ENGINE V1.2")
    print("=====================================================================\n")
    
    # Static calculations baseline
    baseline = AcademicProfile("Suhaib Ali")
    baseline.add_completed_course("MHF4U", 94.0, attempts=3)
    baseline.add_completed_course("MCV4U", 86.0, attempts=1)
    baseline.add_projected_course("ENG4U", 99.0)
    baseline.add_projected_course("HSC4M", 98.0)
    baseline.add_projected_course("BBB4M", 98.0)
    baseline.add_projected_course("BOH4M", 98.0)
    
    print(f"Candidate Profile:        {baseline.student_name}")
    print(f"Calculated Baseline Avg:  {baseline.compile_admission_average():.2f}%\n")
    
    # Interactive Input Shell Loop
    while True:
        try:
            print("\n--- DYNAMIC SIMULATION CONFIGURATION PANEL ---")
            eng_input = input("Enter Expected ENG4U Grade (or 'q' to quit): ").strip()
            if eng_input.lower() == 'q': break
            
            eng_val = float(eng_input)
            cutoff_val = float(input("Enter Waterloo Target Cutoff Baseline % (e.g. 95.5): "))
            
            print("\nCalculating 10,000 empirical tracking models...")
            prob = run_simulation(eng_val, 98.0, 98.0, 98.0, cutoff_val)
            
            print("---------------------------------------------------------------------")
            print(f"SIMULATION RESULTS FOR ENG4U @ {eng_val}% AGAINST {cutoff_val}% CUTOFF:")
            print(f"Calculated Acceptance Probability: {prob:.2f}%")
            print("---------------------------------------------------------------------")
        except ValueError:
            print("[ERROR] Invalid numeric parameters entered. Re-initializing loop context.")
