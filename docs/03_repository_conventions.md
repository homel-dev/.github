# HOMEL REPOSITORY CONVENTIONS
## Repository Organization, Tasks, and Ownership
### Foundational Engineering Specification (Document 03 of 04)
*Namespace: homel-dev • Owner: architecture-team*

---

## Navigation

**Previous:** [02_documentation_style_guide.md](02_documentation_style_guide.md) | **Next:** [04_ci_standard.md](04_ci_standard.md)

- [0. Status, Scope, and Authority](#0-status-scope-and-authority)
- [1. Expected structure](#1-expected-structure)
- [2. Task entry points](#2-task-entry-points)
- [3. Generated files and artifacts](#3-generated-files-and-artifacts)
- [4. Examples](#4-examples)
- [5. Dependency boundaries](#5-dependency-boundaries)
- [6. CI ownership](#6-ci-ownership)
- [7. Closing Statement](#7-closing-statement)

---

## 0. Status, Scope, and Authority

**Status:** IMPLEMENTED
**Audience:** Repository maintainers and contributors
**Change policy:** Update when the shared repository layout or conventions change.

This standard is organization-wide. The checked-in policy and reusable CI workflow provide the reference; repository-specific implementation and validation remain authoritative for runtime behavior.

[Back to top](#navigation)

---

## 1. Expected structure

Repositories SHOULD use a small, predictable top-level structure appropriate
to the project.

Common paths are:

~~~text
README.md
docs/
.github/workflows/
scripts/
tests/
Taskfile.yml
~~~

A repository should not create empty directories merely to match this example.

[Back to top](#navigation)

---

## 2. Task entry points

When a repository uses Task, `Taskfile.yml` MUST parse as a Task v3 document
and operational tasks MUST be children of the top-level `tasks` mapping.

Frequently used validation commands SHOULD have a stable task entry point such
as `task ci:validate`, `task test`, or the repository's documented equivalent.

[Back to top](#navigation)

---

## 3. Generated files and artifacts

Generated local CI output, test output, coverage data, rendered temporary
manifests, and operational captures SHOULD be written to a clearly named
directory and gitignored unless they are intentional release artifacts.

Committed release artifacts MUST be traceable to source state.

[Back to top](#navigation)

---

## 4. Examples

Example credentials MUST use obvious placeholders and MUST never contain live
credentials.

Example manifests SHOULD remain syntactically valid unless the example exists
specifically to demonstrate an invalid case.

[Back to top](#navigation)

---

## 5. Dependency boundaries

Shared organization policy belongs in `homel-dev/.github`.

A repository SHOULD link to shared policy instead of copying it.

Project-specific architecture and operational contracts belong in the project
repository.

[Back to top](#navigation)

---

## 6. CI ownership

Every actively maintained repository SHOULD have a CI workflow.

The organization reusable workflow provides generic repository hygiene.
Repositories remain responsible for domain-specific validation.

A green generic workflow does not establish that an application, Kubernetes
deployment, hardware design, or release artifact is correct.

[Back to top](#navigation)

---

---

## 7. Closing Statement

This document governs the specified organization-wide conventions; project-specific contracts belong in their respective repositories.

[Back to top](#navigation)

---

**END OF DOCUMENT 03**
