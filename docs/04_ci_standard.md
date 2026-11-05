# HOMEL CI STANDARD
## Reusable CI Contract and Security Rules
### Foundational Engineering Specification (Document 04 of 04)
*Namespace: homel-dev • Owner: architecture-team*

---

## Navigation

**Previous:** [03_repository_conventions.md](03_repository_conventions.md) | **Next:** None

- [0. Status, Scope, and Authority](#0-status-scope-and-authority)
- [1. Goals](#1-goals)
- [2. Generic organization checks](#2-generic-organization-checks)
- [3. Workflow security](#3-workflow-security)
- [4. Reusable workflow integration](#4-reusable-workflow-integration)
- [5. Domain-specific CI](#5-domain-specific-ci)
- [6. Closing Statement](#6-closing-statement)

---

## 0. Status, Scope, and Authority

**Status:** IMPLEMENTED
**Audience:** Repository maintainers and CI owners
**Change policy:** Update alongside changes to the shared CI workflow and its validation scripts.

This standard is organization-wide. The checked-in policy and reusable CI workflow provide the reference; repository-specific implementation and validation remain authoritative for runtime behavior.

[Back to top](#navigation)

---

## 1. Goals

CI exists to reject mechanically detectable defects before merge and to make
repository contracts reproducible.

The organization provides:

~~~text
homel-dev/.github/.github/workflows/repository-ci.yml
~~~

This reusable workflow performs generic repository validation. Consumer
repositories add domain-specific jobs.

[Back to top](#navigation)

---

## 2. Generic organization checks

The reusable workflow checks:

- UTF-8 text hygiene;
- trailing whitespace and final newline;
- local Markdown links;
- optional numbered `docs/` filenames;
- obvious committed credential material;
- YAML linting;
- Bash syntax;
- ShellCheck errors;
- GitHub Actions security conventions.

The generic workflow does not deploy applications and does not claim runtime
correctness.

[Back to top](#navigation)

---

## 3. Workflow security

Workflows MUST declare explicit token permissions.

Third-party actions MUST be pinned to full commit SHAs.

`pull_request_target` MUST NOT be used for untrusted code execution.

Checkout credentials SHOULD NOT persist when a job does not need to push.

CI jobs SHOULD be read-only unless a specific release or publication workflow
requires write access.

[Back to top](#navigation)

---

## 4. Reusable workflow integration

A consumer workflow may call:

~~~yaml
jobs:
  standards:
    uses: homel-dev/.github/.github/workflows/repository-ci.yml@main
~~~

Using `@main` is permitted for initial organization bootstrap. Once the shared
workflow is committed and reviewed, important consumers SHOULD replace the
branch reference with that exact `.github` commit SHA.

[Back to top](#navigation)

---

## 5. Domain-specific CI

Repositories MUST add checks appropriate to what they own.

For Kubernetes repositories this normally includes:

- `kubectl kustomize` or equivalent rendering;
- Kubernetes schema validation;
- project-specific topology and policy checks;
- image pin checks;
- resource and persistence checks.

Runtime smoke tests belong in CI only when the required runtime is available
and the test is deterministic. Otherwise they remain an explicit deployment
gate documented by the repository.

[Back to top](#navigation)

---

---

## 6. Closing Statement

This document governs the specified organization-wide conventions; project-specific contracts belong in their respective repositories.

[Back to top](#navigation)

---

**END OF DOCUMENT 04**
