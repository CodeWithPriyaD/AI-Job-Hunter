from models.job import Job
from providers.base_provider import BaseProvider


class MockProvider(BaseProvider):

   def get_jobs(self) -> list[Job]:
        jobs = [

            Job(
                company="Google",
                title="Data Analyst",
                location="Bangalore",
                experience="2-4 Years",
                salary="₹18 LPA",
                source="Mock",
                apply_link="https://careers.google.com",
                posted_date="Today",
                skills=["SQL", "Python", "Excel"]
            ),

            Job(
                company="Microsoft",
                title="Business Analyst",
                location="Hyderabad",
                experience="3 Years",
                salary="₹20 LPA",
                source="Mock",
                apply_link="https://careers.microsoft.com",
                posted_date="Today",
                skills=["Power BI", "SQL"]
            )

        ]

        return jobs
