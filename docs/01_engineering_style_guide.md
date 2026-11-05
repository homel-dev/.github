# HOMEL ENGINEERING STYLE GUIDE
## Organization-Wide Engineering Practices
### Foundational Engineering Specification (Document 01 of 04)
*Namespace: homel-dev • Owner: architecture-team*

---

## Navigation

**Previous:** None | **Next:** [02_documentation_style_guide.md](02_documentation_style_guide.md)

- [0. Status, Scope, and Authority](#0-status-scope-and-authority)
- [1. Scope and authority](#1-scope-and-authority)
- [2. General engineering rules](#2-general-engineering-rules)
- [3. Determinism and reproducibility](#3-determinism-and-reproducibility)
- [4. Configuration and Kubernetes](#4-configuration-and-kubernetes)
- [5. Shell](#5-shell)
- [6. Python](#6-python)
- [7. Security and credentials](#7-security-and-credentials)
- [8. Verification](#8-verification)
- [9. Closing Statement](#9-closing-statement)

---

## 0. Status, Scope, and Authority

**Status:** IMPLEMENTED
**Audience:** Engineers, reviewers, and repository maintainers
**Change policy:** Update with changes to organization engineering requirements and CI behavior.

This standard is organization-wide. The checked-in policy and reusable CI workflow provide the reference; repository-specific implementation and validation remain authoritative for runtime behavior.

[Back to top](#navigation)

---

## 1. Scope and authority

This document defines organization-wide engineering conventions for
`homel-dev`.

Normative terms are used deliberately:

- **MUST** and **MUST NOT** define requirements.
- **SHOULD** and **SHOULD NOT** define the expected default.
- **MAY** defines an allowed option.

A repository may define stricter local policy. A local rule that intentionally
deviates from this guide MUST document the reason and scope of the deviation.

[Back to top](#navigation)

---

## 2. General engineering rules

Changes MUST optimize for correctness, reproducibility, operational
inspectability, and maintainability before cleverness.

Implementation and configuration MUST reflect the documented architecture.
Documentation MUST be changed in the same patch when a behavior, interface,
deployment topology, operational procedure, or ownership boundary changes.

Generated state MUST NOT be treated as source unless the repository explicitly
documents it as authoritative.

Placeholder configuration MUST NOT be presented as production-ready
configuration.

[Back to top](#navigation)

---

## 3. Determinism and reproducibility

Builds, tests, validation, deployment rendering, and release generation SHOULD
be reproducible from repository state.

Versions that materially affect output or runtime behavior SHOULD be pinned.
Container images used by production manifests MUST use explicit tags or
digests; `latest` is prohibited.

GitHub Actions from third-party repositories MUST be pinned to a full commit
SHA. Organization-owned reusable workflows MAY temporarily track a protected
organization branch during bootstrap, but stable consumers SHOULD pin the
workflow to a reviewed commit SHA.

[Back to top](#navigation)

---

## 4. Configuration and Kubernetes

Kubernetes manifests MUST declare explicit namespaces or be rendered by a
namespace-scoped Kustomization.

Long-running workload containers MUST declare CPU and memory requests and
limits unless a repository-specific document explains why a limit would be
unsafe.

Persistent services MUST make retention and storage behavior explicit.

RBAC MUST use the least privilege practical for the workload.

NetworkPolicy MUST be explicit where a workload crosses namespace or trust
boundaries. A policy must not claim isolation that has not been validated
against the actual CNI and network topology.

Secrets MUST NOT be committed. Examples must contain unmistakable placeholders.

[Back to top](#navigation)

---

## 5. Shell

Executable shell scripts MUST:

- use a declared interpreter;
- use `set -euo pipefail` for non-trivial Bash automation unless there is a
  documented reason not to;
- quote variable expansions unless word splitting is intentional;
- fail with a non-zero exit status when validation fails;
- avoid parsing human-formatted output when a machine-readable interface is
  available.

Shell CI MUST run syntax validation. ShellCheck SHOULD run at least at error
severity.

[Back to top](#navigation)

---

## 6. Python

Python automation SHOULD use the standard library when practical and SHOULD
keep dependencies explicit when external packages are required.

Validation tools MUST produce actionable errors that identify the file and
condition that failed.

Scripts that inspect repository state MUST avoid following symlinks outside the
repository root.

[Back to top](#navigation)

---

## 7. Security and credentials

Repository automation MUST use minimum GitHub token permissions.

Pull-request validation MUST NOT require production credentials.

Private keys, access tokens, passwords, cloud credentials, and live service
credentials MUST NOT be committed.

CI MUST NOT echo secrets or derived credentials.

[Back to top](#navigation)

---

## 8. Verification

A change is not complete merely because configuration parses.

Repositories MUST validate the semantics relevant to their domain. Examples
include:

- rendering and schema-validating Kubernetes manifests;
- running unit and integration tests;
- validating generated artifacts;
- exercising smoke paths for deployed services;
- checking invariants that generic syntax tools cannot express.

CI is a gate, not documentation of intent. Repository documentation must still
describe the invariant being enforced.

[Back to top](#navigation)

---

---

## 9. Closing Statement

This document governs the specified organization-wide conventions; project-specific contracts belong in their respective repositories.

[Back to top](#navigation)

---

**END OF DOCUMENT 01**
