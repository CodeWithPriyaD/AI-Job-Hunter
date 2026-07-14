from model.job import Job

job = Job(
    company="ABC Corp",
    title="Software Engineer",
    location="New York",
    experience="5 years",
    salary="$100,000",
    source="LinkedIn",
    apply_link="https://linkedin.com/jobs/view/software-engineer-at-abc-corp",
    posted_date="2023-10-01",
    skills=["Python", "JavaScript", "SQL"],
    score=95,
    applied=False
)

print(job)

