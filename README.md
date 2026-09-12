# Synthetic Website Analytics Platform

An end-to-end, reproducible analytics platform for a synthetic ecommerce-style
website. It turns configurable visitor behavior into trusted analytical marts
and answers practical questions about acquisition, conversion, and navigation.

## Why this project exists

Production analytics work is rarely a single notebook or dashboard. This
portfolio project demonstrates the complete path from source generation through
data modeling to analysis, using a dataset that is safe to share and easy to
recreate.

## Platform architecture

```text
Configurable visitor, session, and campaign simulation
                         |
                         v
 synthetic-website-data: files + PostgreSQL raw tables
                         |
                         v
 synthetic-website-dbt: staging, intermediate, and mart models
                         |
                         v
synthetic-website-analytics: SQL queries and exploratory analysis
```

## Component repositories

| Repository | Responsibility | Highlights |
| --- | --- | --- |
| [synthetic-website-data](https://github.com/SpencerRWood/synthetic-website-data) | Generates deterministic event streams and loads raw PostgreSQL sources. | Typed Python, configuration-driven scenarios, migrations, tests, Docker, optional Dagster orchestration. |
| [synthetic-website-dbt](https://github.com/SpencerRWood/synthetic-website-dbt) | Transforms raw events into documented analytical marts. | Staging/intermediate/mart layers, data-quality tests, SQLFluff, Docker. |
| [synthetic-website-analytics](https://github.com/SpencerRWood/synthetic-website-analytics) | Investigates the modeled data and communicates findings. | Reusable SQL, database utilities, notebooks, and tests. |

## What it demonstrates

- Deterministic, configurable generation of visitor journeys, events, campaigns,
  and a website navigation graph.
- Warehouse-style modeling that turns raw events into session, visitor,
  campaign, funnel, and navigation marts.
- Analytical workflows for daily performance, campaign effectiveness,
  conversion, and observed page-to-page movement.
- Reproducible local development using `uv`, Docker, PostgreSQL, and automated
  checks in every component repository.

## Quick start

Follow the repositories in order:

1. Set up and run `synthetic-website-data` to generate and load the raw data.
2. Run `dbt build` in `synthetic-website-dbt` to create the analytical marts.
3. Run a query or open the notebook in `synthetic-website-analytics`.

Each component owns its environment configuration and detailed setup steps.
See [architecture](docs/architecture.md) for boundaries and data flow, and the
[roadmap](docs/roadmap.md) for planned extensions.

## Design principles

The platform keeps concerns deliberately separate: generation owns raw data,
dbt owns transformations, and analytics owns downstream interpretation. This
makes each repository independently understandable while keeping the full
workflow reproducible.

## Status

The platform is actively evolving. The current scope is an analytical foundation
for website behavior; it intentionally does not claim to be a production web
application, tracking SDK, or BI product.

## License

Each component repository is released under the MIT License.
