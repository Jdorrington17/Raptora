# Public repository activity and monitoring

This repository is public by design. Public availability does **not** imply that viewers, downloaders or cloners can be identified.

## What can be observed
- Stars and forks: public accounts that interact through supported GitHub events.
- Issues, pull requests and comments: public actor, timestamps and review history.
- GitHub Insights → Traffic: aggregate visitor and clone counts over GitHub's limited recent reporting window (typically 14 days), available to users with the necessary repository privileges.
- Notifications and audit logs: maintainers can watch GitHub notifications, Actions runs and repository settings as applicable.

## Automated metadata audit
Once merged into the default branch, `.github/workflows/public-activity.yml` records supported interaction-event metadata in GitHub Actions run output: event type, action, public GitHub username, timestamp, and whether the actor differs from the repository owner.

It does **not** execute outsider-submitted code, capture comment/issue bodies, capture IP addresses, identify anonymous visitors, or provide a permanent analytics database. Workflow runs/logs are retained according to repository settings; some events only occur when the workflow is present on the default branch, and not every unstar/unwatch action produces a matching event.

A non-owner is **not necessarily an unauthorised contributor**. Evaluate rights based on repository permissions and accepted review process, not a username comparison.

## Recommended maintainer review
- Check Notifications for outside issues, PRs and security reports.
- Check Insights → Traffic regularly before GitHub's short history expires.
- Review forks and watchers/stargazers where visible.
- Review Actions runs for `Public interaction audit`.
- Reject unreviewed changes and maintain minimum workflow permissions.
- Treat GitHub event records as limited engagement indicators, not complete visitor surveillance.

Never insert third-party web tracking, IP beacons or executable code into contributors' work merely to identify people.
