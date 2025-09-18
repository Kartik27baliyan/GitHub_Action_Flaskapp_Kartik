# Flask CI/CD Pipeline with GitHub Actions

This project demonstrates a continuous integration and deployment (CI/CD) pipeline for a Flask application using GitHub Actions.

## 📋 Workflow Description

The `.github/workflows/ci_cd.yml` file defines the pipeline:

### 🔧 Jobs Overview:

1.  **Test**: Triggered on pushes to `main`/`staging` and pull requests to `main`
    - Tests the application against Python 3.9, 3.10, and 3.11
    - Installs dependencies from `requirements.txt`
    - Runs tests using `pytest`

2.  **Deploy to Staging**: Triggered on pushes to the `staging` branch
    - Only runs if the `test` job succeeds
    - Uses the `staging` environment with protection rules
    - Requires branch restriction: only `staging` branch can deploy

3.  **Deploy to Production**: Triggered when a new release is published
    - Only runs if the `test` job succeeds
    - Uses the `production` environment with protection rules

## 🛠️ Setup Instructions

### Environment Configuration:
1.  **Environments**: Configured `staging` and `production` in Repository Settings
2.  **Secrets**: Added `STAGING_DEPLOY_KEY` and `PRODUCTION_DEPLOY_KEY` as environment secrets
3.  **Branch Restrictions**: Set deployment rules to only allow `staging` branch for staging environment

### Branch Structure:
- `main`: Development and testing branch
- `staging`: Staging deployment branch
- Releases: Production deployments via GitHub Releases

## 📊 Workflow Triggers

| Event | Trigger | Actions |
|-------|---------|---------|
| Push to `main` | ✅ | Runs tests |
| Push to `staging` | ✅ | Runs tests → Deploys to staging |
| Pull Request to `main` | ✅ | Runs tests |
| New Release Published | ✅ | Runs tests → Deploys to production |

## 🔒 Security Features
- Environment-specific secrets
- Branch deployment restrictions
- Required reviewers (optional)
- Wait timers for deployment safety

# GitHub_Action_Flaskapp_Kartik
CI/CD workflow using GitHub Actions for a Python application.
Prepairing to launch!

