Example Builder input after assessment GO:

```text
/corporate-context
We need to allow authenticated suppliers to update contact and address data. CNPJ must remain immutable and all changes need auditability.
```

Then:

```text
/speckit.specify
Allow an authenticated supplier to update phone, email and address. CNPJ cannot be changed after onboarding. Every accepted change must be auditable. If an update fails, the system must not persist partial changes.
```
