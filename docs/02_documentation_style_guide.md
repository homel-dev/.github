# HOMEL DOCUMENTATION STYLE GUIDE AND STANDARD
## Formatting, Authority, Navigation, and Maintenance Rules
### Foundational Engineering Specification (Document 02 of 04)
*Namespace: homel-dev • Owner: architecture-team*

---

## Navigation

**← [Previous: Document 01 (Engineering Style Guide)](01_engineering_style_guide.md) | [Next: Document 03 (Repository Conventions)](03_repository_conventions.md) →**

- [0. Status, Scope, and Authority](#0-status-scope-and-authority)
- [1. Purpose](#1-purpose)
- [2. Authority and Drift Policy](#2-authority-and-drift-policy)
- [3. File Naming and Organization](#3-file-naming-and-organization)
- [4. Header and Metadata Standard](#4-header-and-metadata-standard)
- [5. Navigation and Interlinking](#5-navigation-and-interlinking)
- [6. Typography and Formatting](#6-typography-and-formatting)
- [7. Tone and Normative Language](#7-tone-and-normative-language)
- [8. Section Standardization](#8-section-standardization)
- [9. Visual Representation Standard](#9-visual-representation-standard)
- [10. Completeness Standard](#10-completeness-standard)
- [11. Code-to-Documentation Authority Map](#11-code-to-documentation-authority-map)
- [12. Repository Documentation Set](#12-repository-documentation-set)
- [13. Normative Status Rules](#13-normative-status-rules)
- [14. Documentation Review Procedure](#14-documentation-review-procedure)
- [15. Diagram Rules in Detail](#15-diagram-rules-in-detail)
- [16. Examples and Command Safety](#16-examples-and-command-safety)
- [17. Closing Statement](#17-closing-statement)

---

## 0. Status, Scope, and Authority

**Status:** IMPLEMENTED  
**Audience:** All contributors and maintainers  
**Change policy:** Living implementation-aligned standard; no silent behavioral drift.

This document defines the organization-wide documentation standard for `homel-dev` engineering specifications and repository operational guides.

[Back to top](#navigation)

---

## 1. Purpose

Documentation MUST remain readable, navigable, technically precise, and synchronized with the current repository.

The standard exists to enforce:

- uniform visual hierarchy;
- deterministic cross-linking and anchors;
- explicit implementation status;
- engineering tone without marketing filler;
- maintainable Mermaid diagrams instead of opaque screenshots for architecture.

[Back to top](#navigation)

---

## 2. Authority and Drift Policy

The checked-in implementation and executable tests are the authority for current runtime behavior.

Documentation MUST describe behavior present in the current tree. A design that is not implemented MUST be labelled `PROPOSAL`, `PARTIAL`, `BACKGROUND`, `DEPRECATED`, or otherwise explicitly non-runtime. Documentation MUST NOT make an unimplemented behavior canonical merely by describing it.

Behavior-changing code changes MUST update every affected documentation contract in the same change set. Historical decisions belong in Git history, ADRs, or explicitly dated notes; stale current-state text MUST be edited rather than preserved behind an append-only rule.

Allowed status values:

- `IMPLEMENTED` — represented by current code/manifests and, where practical, executable tests;
- `PARTIAL` — only the explicitly identified subset exists;
- `PROPOSAL` — design intent only;
- `BACKGROUND` — rationale/comparison material, not a runtime contract;
- `DEPRECATED` — retained only for migration/history.

[Back to top](#navigation)

---

## 3. File Naming and Organization

Numbered engineering specifications under `docs/` MUST use `NN_topic_slug.md` with a two-digit index and lowercase underscore-separated slug.

Repository-root operational guides such as `README.md`, `DEPLOYMENT.md`, and `CONTRIBUTING.md` MAY use conventional root filenames but MUST follow the same formatting, tone, and authority rules where applicable.

Architecture images SHOULD be represented as Mermaid source. If binary assets are required, they MUST live under a documented assets directory and MUST NOT duplicate a maintainable Mermaid representation without reason.

[Back to top](#navigation)

---

## 4. Header and Metadata Standard

Numbered engineering specifications MUST begin with:

~~~markdown
# [DOCUMENT TITLE IN CAPS]
## [Descriptive Subtitle]
### Foundational Engineering Specification (Document XX of YY)
*Namespace: [repository-or-organization] • Owner: [owner]*

---
~~~

Proposal/background documents MAY replace the third line with an explicit `Engineering Proposal` or `Background Architecture Note`, but status MUST remain unambiguous.

[Back to top](#navigation)

---

## 5. Navigation and Interlinking

Every numbered specification MUST contain a `## Navigation` section immediately after the header separator.

The navigation section MUST contain:

- directional previous/next links where applicable;
- a manual table of contents using repository-stable GitHub/GitLab-compatible anchor slugs;
- explicit filenames in links.

At the end of every major H2 section, insert:

~~~markdown
[Back to top](#navigation)
~~~

Links MUST be relative when the target is in the same repository.

[Back to top](#navigation)

---

## 6. Typography and Formatting

### 6.1 Code Blocks

Repository documentation MUST use triple tildes and MUST specify a language identifier:

~~~markdown
~~~bash
command
~~~
~~~

Use `text` for pseudo-code and traces. Triple backtick fences are non-compliant in committed engineering specifications.

When an entire Markdown document is reprinted in chat/tickets and contains internal triple-tilde fences, an outer quadruple-tilde fence MAY be used to avoid delimiter collision. That exception does not apply to committed files.

### 6.2 Tables

Use standard GFM tables. Text SHOULD be left-aligned unless numeric/status alignment materially improves readability.

### 6.3 Invariants and Warnings

Use standard Markdown blockquotes:

~~~markdown
> **Hard Invariant:** The component MUST NOT cross its documented authority boundary.
~~~

Do not use proprietary alert syntax.

### 6.4 Generated Artifacts

Do not commit generated citation markers, transcript annotations, or model-output metadata such as `[cite_start]` or `[cite: ...]`.

[Back to top](#navigation)

---

## 7. Tone and Normative Language

Use RFC 2119-style `MUST`, `MUST NOT`, `SHOULD`, and `MAY` for normative requirements.

Documentation MUST be concise, active-voice, and implementation-specific. Avoid conceptual filler such as “basically”, “kind of”, or aspirational language that is indistinguishable from current behavior.

Commands, endpoints, environment variables, table names, and workload names SHOULD be written exactly as implemented.

[Back to top](#navigation)

---

## 8. Section Standardization

Every numbered specification MUST begin its body with:

~~~markdown
## 0. Status, Scope, and Authority

**Status:** IMPLEMENTED / PARTIAL / PROPOSAL / BACKGROUND / DEPRECATED
**Audience:** [target roles]
**Change policy:** [explicit maintenance rule]
~~~

Every numbered specification MUST end with a `Closing Statement`, a separator, and an `END OF DOCUMENT` marker.

[Back to top](#navigation)

---

## 9. Visual Representation Standard

Architecture and sequence diagrams MUST use Mermaid when a diagram materially improves understanding.

Diagrams MUST show current deployable units and real request paths. Proposed components or flows MUST be marked as proposed in both diagram labels and surrounding text.

Use C4 concepts for system/container/component boundaries even when standard Mermaid `flowchart` or `sequenceDiagram` syntax is more practical than a C4-specific renderer.

For flowcharts, top-to-bottom layout (`flowchart TB`) SHOULD be preferred unless the represented topology materially requires another direction.

[Back to top](#navigation)

---

## 10. Completeness Standard

A documentation update is not complete merely because every file exists. The repository documentation set MUST preserve enough detail for an engineer who has not read the implementation to understand the runtime boundaries, data movement, operational entry points, failure behavior, and verification path.

For each behavior-changing subsystem, documentation SHOULD cover all of the following dimensions when they apply:

1. purpose and authority;
2. inputs and outputs;
3. persistence and mutation behavior;
4. runtime configuration;
5. request or event sequence;
6. failure handling and fallbacks;
7. observability and diagnostics;
8. operator workflow;
9. executable verification;
10. explicit non-implemented or proposal-only behavior.

Short summaries MAY appear in the root README and cheat sheet, but numbered engineering documents MUST retain the detailed contract. A rewrite MUST NOT collapse a detailed specification into a marketing summary when the removed material is still relevant to operating, extending, or reviewing the system.

[Back to top](#navigation)

---

## 11. Code-to-Documentation Authority Map

Repositories with multiple implementation and documentation surfaces SHOULD maintain a clear mapping between source areas and their primary documentation contracts.

A typical mapping is:

| Implementation area | Primary documentation | Required synchronization |
| --- | --- | --- |
| Runtime APIs, schemas, routing, and request handling | Architecture and runtime-contract documents | Update interface contracts, request semantics, topology, and failure behavior |
| Kubernetes manifests and operational Taskfiles | Runtime and deployment documentation | Update service names, ports, environment/configuration, images, lifecycle, and health procedures |
| Persistent storage and schema definitions | Storage and data-contract documentation | Update schema inventory, ownership, retention, and active runtime behavior |
| Telemetry collectors and exporters | Observability documentation | Update signal paths, endpoints, labels, dashboards, retention, and diagnostics |
| Operator and administrative interfaces | Operations documentation | Update discovery, invocation, permissions, and failure procedures |
| CI workflows and tests | Verification and contribution documentation | Update exact checks, validation entry points, and definition of done |

A repository-specific authority map MAY be more detailed when the implementation requires it.

[Back to top](#navigation)

---

## 12. Repository Documentation Set

The maintained documentation surface varies by repository. Root guides, numbered specifications, architecture background material, and component READMEs have different purposes and SHOULD NOT duplicate each other verbatim.

When present, these file families normally serve the following roles:

| File family | Audience | Expected depth |
| --- | --- | --- |
| `README.md` | New users and maintainers | Architecture summary, supported workflows, limits, documentation map |
| `ARCHITECTURE_CHEAT_SHEET.md` | Operators/reviewers | Compact but precise runtime reference |
| `CONTRIBUTING.md` | Contributors | Engineering workflow, boundaries, tests, documentation duties |
| `DEPLOYMENT.md` | Operators | Runnable lifecycle and troubleshooting procedures |
| `RFC_PROPOSAL.md` | Architects | Architectural rationale with current/proposal distinction |
| `docs/NN_*.md` | Implementers/operators | Detailed normative or explicitly scoped background/proposal contracts |
| `docs/WHITEPAPER.md` | Architects/stakeholders | Background narrative anchored to current implementation |
| `components/*/README.md` | Component maintainers | Local responsibilities, APIs, dependencies, tests, operational notes |

Repositories SHOULD include only documentation surfaces that correspond to an actual maintenance or operational need.

[Back to top](#navigation)

---

## 13. Normative Status Rules

Use one of these status meanings consistently:

- **IMPLEMENTED**: code/manifests exist in the current tree and the document describes that behavior.
- **PARTIAL**: a bounded subset exists; the document MUST name both the implemented and missing pieces.
- **PROPOSAL**: design intent only. It MUST NOT be described as an existing runtime guarantee.
- **BACKGROUND**: explanatory or comparative material, not a runtime contract.
- **DEPRECATED**: retained for migration/history and not recommended for new use.

A database table created by a migration is **provisioned schema**, not proof that a control loop is implemented. A configuration key that can be written is **not active configuration** unless a current consumer reads it. A documented command is **not supported** unless its referenced Task, route, tool, script, or executable entry point exists in the current tree.

[Back to top](#navigation)

---

## 14. Documentation Review Procedure

Before merging a documentation-sensitive change, a reviewer SHOULD perform this sequence:

1. identify the source files and manifests changed by the implementation;
2. map them to the relevant documentation contracts;
3. inspect every affected public API, environment variable, Task, schema, tool, and operator step;
4. search documentation for the old name or behavior and update every current-state reference;
5. mark design-only sections explicitly rather than silently deleting useful rationale;
6. verify local Markdown links;
7. verify one H1 per Markdown file;
8. verify no trailing whitespace and a final newline;
9. run the organization repository policy and YAML/Shell checks when applicable;
10. compare the resulting documentation depth against the pre-change contract so detail is not accidentally discarded.

[Back to top](#navigation)

---

## 15. Diagram Rules in Detail

Mermaid diagrams SHOULD encode authority and direction, not decorative complexity. A diagram SHOULD state which component performs a write when the distinction matters. Data stores SHOULD be named by role rather than merely by product. Proposed components MUST be visually or textually identified as proposed.

Recommended diagram forms:

- flowchart for component/topology boundaries;
- sequence diagram for request, admission, or agent workflows;
- state diagram only when an actual state machine exists;
- table instead of a diagram when exact field or flag behavior is more important than topology.

Flowcharts SHOULD use a top-to-bottom layout unless another orientation materially improves the representation of the actual system.

[Back to top](#navigation)

---

## 16. Examples and Command Safety

Examples MUST be copyable or clearly marked pseudocode. Destructive commands MUST be identified as destructive. Secrets MUST use placeholders and MUST NOT be embedded in committed examples.

Host-side commands MUST NOT be presented as required when the repository provides a checked-in wrapper or task entry point for the same operation.

Commands, task names, namespaces, service names, routes, and tool names used in examples MUST exist in the repository being documented unless the example is explicitly marked as pseudocode.

[Back to top](#navigation)

---

## 17. Closing Statement

Organization documentation is trustworthy only when engineers can distinguish implemented behavior from design intent and can navigate from code and manifests to documentation without encountering contradictory contracts.

[Back to top](#navigation)

---

**END OF DOCUMENT 02**
