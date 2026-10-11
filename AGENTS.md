# Repository Guidance

## Purpose and boundaries
- This is the cross-repository architecture and roadmap for the synthetic website analytics platform.
- `synthetic-website-data` generates events, `synthetic-website-dbt` models them, and `synthetic-website-analytics` interprets them.

## Development
- Update `README.md`, `docs/architecture.md`, and `docs/roadmap.md` together when platform boundaries change.
- Link to implementation repositories rather than copying their detailed setup instructions here.

## Validation
- Check Markdown links and referenced repository paths when editing platform documentation.
- There is no package build or test command configured in this repository.

## Architecture constraints
- Keep ownership and data flow explicit across generator, transformations, and analysis.
- Avoid declaring an implementation complete based only on the roadmap.

## Safety
- Do not add credentials, environment-specific connection details, or generated datasets to architecture docs.

## Branching strategy

- This repository uses **trunk-based development**. Create short-lived change branches from current `main` and target PRs to `main`.
- Follow the [canonical branching and delivery policy](https://github.com/SpencerRWood/codex-config/blob/main/docs/branching-policy.md), available through the installed codex-config source path. Verify the strategy, release association, fetched base and PR target before implementation and record them in Story evidence. Story completion does not authorize publication or deployment; retain existing review, CI, security and rollback requirements.
