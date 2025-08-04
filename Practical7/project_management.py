from project import Project

FILENAME = "projects.txt"


def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        file.readline()  # skip header
        for line in file:
            parts = line.strip().split('\t')
            projects.append(Project(*parts))
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=file)
        for p in projects:
            print(f"{p.name}\t{p.start_date.strftime('%d/%m/%Y')}\t{p.priority}\t{p.cost_estimate}\t{p.completion_percentage}", file=file)


def display_projects(projects):
    print("Incomplete projects: ")
    for p in sorted([p for p in projects if not p.is_complete()]):
        print(f"  {p}")
    print("Completed projects: ")
    for p in sorted([p for p in projects if p.is_complete()]):
        print(f"  {p}")


def filter_by_date(projects):
    date_str = input("Show projects that start after date (dd/mm/yyyy): ")
    date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    filtered = [p for p in projects if p.start_date > date]
    for p in sorted(filtered, key=lambda x: x.start_date):
        print(p)


def add_project():
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion = input("Percent complete: ")
    return Project(name, start_date, priority, cost_estimate, completion)


def update_project(projects):
    for i, p in enumerate(projects):
        print(f"{i} {p}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)
    new_completion = input("New Percentage: ")
    new_priority = input("New Priority: ")
    project.update(new_completion, new_priority)


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    while True:
        print("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit")
        choice = input(">>> ").lower()
        if choice == 'l':
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_by_date(projects)
        elif choice == 'a':
            projects.append(add_project())
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            if input("Would you like to save to projects.txt? ").lower() in ["yes", "y"]:
                save_projects(FILENAME, projects)
            print("Thank you for using custom-built project management software.")
            break


if __name__ == '__main__':
    main()