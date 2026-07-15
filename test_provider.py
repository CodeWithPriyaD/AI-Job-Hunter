from providers.mock_provider import MockProvider

provider = MockProvider()

jobs = provider.get_jobs()

for job in jobs:
    print("-------------------")
    print(job.company)
    print(job.title)
    print(job.location)
    print(job.salary)