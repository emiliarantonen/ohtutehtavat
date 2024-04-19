class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        authors_print=""
        for author in self.authors:
            authors_print+=f"- {author}\n"

        dependencies_print=""
        for d in self.dependencies:
            dependencies_print+=f"- {d}\n"
        
        dev_dependencies_print=""
        for dd in self.dev_dependencies:
            dev_dependencies_print+=f"- {dd}\n"
        
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}\n"
            f"\nauthors:\n {authors_print}\n"
            f"\nDependencies:\n {dependencies_print}\n"
            f"\nDevelopment dependencies:\n {dev_dependencies_print}"
        )
