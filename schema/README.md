# Schema

The Commons FinOps machine-readable specifications.

- [`SCHEMA.md`](./SCHEMA.md) — the funding-block v0.1 specification in plain language.
- [`funding-block-v0.1.yaml`](./funding-block-v0.1.yaml) — the canonical schema reference.
- [`validator.py`](./validator.py) — working Python validator. Run with `python3 validator.py <file.yaml>`.
- [`examples/`](./examples) — four worked example fixtures.

To validate the example fixtures:

```bash
python3 validator.py examples/01-template.yaml examples/02-metagov-sample.yaml examples/03-broken-allocation.yaml examples/04-astropy-partial.yaml
```

Expected output: template warns about placeholder, sample passes, broken example errors on two fields, AstroPy partial errors on four missing required fields.
