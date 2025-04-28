from dataclasses import dataclass

@dataclass
class Student:
    student_id: str
    name: str
    mobile_number: str
    email: str
    gpa: float
    specialization: str
    preferred_locations: list
    skills: list

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "mobile_number": self.mobile_number,
            "email": self.email,
            "gpa": self.gpa,
            "specialization": self.specialization,
            "skills": ",".join(self.skills),
            "preferred_location_1": self.preferred_locations[0] if len(self.preferred_locations) > 0 else "",
            "preferred_location_2": self.preferred_locations[1] if len(self.preferred_locations) > 1 else "",
            "preferred_location_3": self.preferred_locations[2] if len(self.preferred_locations) > 2 else ""
        }

@dataclass
class ApprenticeshipOpening:
    specialization: str
    location: str
    stipend: float
    required_skills: list

    def to_dict(self):
        return {
            "specialization": self.specialization,
            "location": self.location,
            "stipend": self.stipend,
            "required_skills": ",".join(self.required_skills)
        }
