# Homel Documentation Style Guide

## 1. Purpose

Documentation is part of the implementation contract. It must describe the
system that exists, not a historical approximation of it.

## 2. Repository entry point

The repository root SHOULD contain `README.md`.

The README SHOULD answer, in this order:

1. what the project is;
2. what problem it owns;
3. the high-level architecture;
4. how to deploy, run, or use it;
5. how to validate it;
6. where the canonical detailed documentation lives.

The README should remain an entry point rather than duplicate every design
document.

## 3. Documentation files

Canonical project documents SHOULD live under `docs/`.

Repositories using ordered architecture documentation SHOULD name canonical
documents:

```text
NN_topic_slug.md
```

where `NN` is a two-digit order number.

Renumbering documents solely for aesthetics is discouraged because it breaks
links and review history.

## 4. Markdown

Documentation MUST be plain Markdown stored in the repository.

Use one level-1 heading per document. Heading levels SHOULD reflect actual
structure rather than visual preference.

Commands, configuration, code, JSON, YAML, and terminal output MUST use fenced
code blocks with an appropriate language identifier when one exists.

Relative links SHOULD be used for files inside the same repository.

Links to local files MUST resolve.

## 5. Diagrams

Architecture, process, sequence, state, and dependency diagrams MUST use
Mermaid when the diagram can be represented clearly in Mermaid.

ASCII art MUST NOT be used as a substitute for an architecture diagram.

Text code blocks MAY still represent literal directory trees, protocol payloads,
command output, or exact text formats; those are examples, not diagrams.

A diagram MUST agree with the surrounding prose and the implementation.

## 6. Tables

Use tables for genuinely tabular comparisons, contracts, matrices, and compact
inventories.

Do not force narrative explanations into wide tables.

## 7. Normative language

Use `MUST`, `MUST NOT`, `SHOULD`, `SHOULD NOT`, and `MAY` only when the text is
intended to be normative.

Hard invariants SHOULD be stated explicitly and near the architecture they
constrain.

## 8. Operational documentation

Operational procedures MUST distinguish:

- deployment from validation;
- health from mere process existence;
- destructive from non-destructive actions;
- desired state from observed state;
- persistent state from disposable state.

If a command can delete retained data, credentials, or persistent volumes, the
documentation MUST make that consequence explicit.

## 9. Drift

When implementation changes, affected documentation MUST be updated in the
same patch.

Superseded architecture SHOULD be either updated in place or clearly marked as
superseded and linked to the current authority. Contradictory documents must
not both appear current.
