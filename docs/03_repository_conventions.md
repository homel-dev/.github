# Homel Repository Conventions

## 1. Expected structure

Repositories SHOULD use a small, predictable top-level structure appropriate
to the project.

Common paths are:

```text
README.md
docs/
.github/workflows/
scripts/
tests/
Taskfile.yml
```

A repository should not create empty directories merely to match this example.

## 2. Task entry points

When a repository uses Task, `Taskfile.yml` MUST parse as a Task v3 document
and operational tasks MUST be children of the top-level `tasks` mapping.

Frequently used validation commands SHOULD have a stable task entry point such
as `task ci:validate`, `task test`, or the repository's documented equivalent.

## 3. Generated files and artifacts

Generated local CI output, test output, coverage data, rendered temporary
manifests, and operational captures SHOULD be written to a clearly named
directory and gitignored unless they are intentional release artifacts.

Committed release artifacts MUST be traceable to source state.

## 4. Examples

Example credentials MUST use obvious placeholders and MUST never contain live
credentials.

Example manifests SHOULD remain syntactically valid unless the example exists
specifically to demonstrate an invalid case.

## 5. Dependency boundaries

Shared organization policy belongs in `homel-dev/.github`.

A repository SHOULD link to shared policy instead of copying it.

Project-specific architecture and operational contracts belong in the project
repository.

## 6. CI ownership

Every actively maintained repository SHOULD have a CI workflow.

The organization reusable workflow provides generic repository hygiene.
Repositories remain responsible for domain-specific validation.

A green generic workflow does not establish that an application, Kubernetes
deployment, hardware design, or release artifact is correct.
