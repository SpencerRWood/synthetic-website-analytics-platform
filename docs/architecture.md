# Architecture

## Data flow

```text
Scenario YAML
    |
    v
Python generator
    |-- CSV and JSON exports
    `-- PostgreSQL raw.events, raw.campaigns, raw.website
                              |
                              v
                           dbt models
    raw -> staging -> intermediate -> marts
                              |
                              v
                    SQL queries and notebooks
```

The generator emits synthetic visitor and session journeys along with campaign
and website-graph context. dbt preserves source fidelity in staging, derives
reusable session and visitor logic in intermediate models, and exposes
analytics-ready facts and dimensions in marts.

## Repository boundaries

| Layer | Owns | Does not own |
| --- | --- | --- |
| Data generation | Simulation rules, raw source schemas, file exports, ingestion | Business-facing aggregation and interpretation |
| dbt | Transformations, mart contracts, data-quality assertions | Source simulation or downstream dashboards |
| Analytics | Analysis queries, notebooks, and conclusions | Raw-data generation or transformation infrastructure |

This separation lets the platform evolve without hiding key logic in a single,
large repository.
