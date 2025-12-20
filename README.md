# platform-app-templates

Approved application scaffolding templates for the “New Application Scaffold” Coder Task.

## Goals

- Provide deterministic, repeatable scaffolds for:
  - Python
  - React
  - Go
- Ensure every template ships with:
  - A minimal, working application
  - A Dockerfile
  - A Helm chart for Kubernetes deployment
  - An Argo CD `Application` manifest (`argocd/apps.yaml`) that points Argo CD at the app repository
- Keep values inside the application repository (simpler demo; single-source Argo CD).

## Repository layout

- `templates/index.yaml`
  - Machine-readable catalog used by the Coder Task to choose the correct template.
- `templates/<language>/<template-name>/`
  - Individual templates.
- `shared/branding/`
  - Shared styling tokens you can copy into generated apps.

## Template contract

Each template directory MUST contain:

- `template.yaml`
- `app/` (or `src/` for React)
- `tests/` (where applicable)
- `Dockerfile`
- `helm/`
- `argocd/apps.yaml`

## Placeholder contract

Some files include placeholders that the Coder Task MUST replace when generating an app repository.

- `__APP_NAME__`
  - Example: `demo-python-profile`
- `__NAMESPACE__`
  - Example: `app-demo-python-profile`
- `__REPO_URL__`
  - Example (SSH): `git@git.globallogic.local:sirlegendary/demo-python-profile.git`
- `__ARGOCD_NAMESPACE__`
  - Example: `argocd`
- `__ARGOCD_PROJECT__`
  - Example: `default`
- `__VALUES_FILE__`
  - Example: `values.yaml` (in Helm chart)
- `__IMAGE_REPO__`
  - Example: `gitea.globallogic.local/sirlegendary/demo-python-profile`
- `__IMAGE_TAG__`
  - Example: `latest`
- `__INGRESS_HOST__`
  - Example: `demo-python-profile.globallogic.local`

## Adding new templates

- Add a new folder under `templates/<language>/...`
- Add an entry in `templates/index.yaml`
- Keep the Helm chart and Argo CD app manifest consistent with existing templates
