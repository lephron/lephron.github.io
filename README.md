# Lephron Games · Fishito

Public static developer site at **https://lephron.github.io/**. HTML and CSS only: no application server, analytics, remote fonts, cookies added by us, or form database. GitHub Pages still processes visitor request information for hosting/security.

## Store listing URLs

| Field | Value |
| --- | --- |
| Developer website / Apple marketing URL | `https://lephron.github.io/` |
| Privacy policy | `https://lephron.github.io/privacy.html` |
| Support URL | `https://lephron.github.io/support.html` |
| Account/data deletion request URL | `https://lephron.github.io/delete-account.html` |
| Public support/privacy email | `lephron.studios@gmail.com` |
| AdMob seller file | `https://lephron.github.io/app-ads.txt` |

See [RELEASE-CHECKLIST.md](RELEASE-CHECKLIST.md) for remaining store, game, and operator work. These files prepare the website; they do not configure store listings, enable ads/payments, or implement automatic account deletion.

## Hosting and development

GitHub Pages publishes `main` from the repository root. `.nojekyll` preserves the plain files. Changes should use a feature branch and pull request. The small Actions workflow audits links/metadata; GitHub's Pages build performs publication after merge.

```sh
python3 scripts/check_site.py
python3 -m http.server 4173
```

Open `http://localhost:4173`. Stop the server with Ctrl+C. No package installation or build step is needed. To audit whether ads can be authorized, run `python3 scripts/check_site.py --require-ads`; this deliberately fails until the owner's real AdMob seller entry is present.

## AdMob activation is pending

The owner has not yet supplied an AdMob publisher ID. `app-ads.txt` is currently comment-only: its public endpoint exists, but **it does not authorize ad serving or complete verification**. Copy the exact personalized line from AdMob → Apps → View all apps → app-ads.txt → How to set up app-ads.txt. Replace the comments, run the strict check, merge a PR, and request verification in AdMob after linking the published store listing. Never use Google's sample publisher ID, invented digits, an app ID (`~`), or an ad-unit ID (`/`).

Official instructions: https://support.google.com/admob/answer/9363762?hl=en

## Content ownership and maintenance

Logo and three species PNGs are copied unchanged from Fishito's existing approved artwork. The website's policy reflects the inspected implementation on 13 October 2026, including schema-8 progress, platform authentication, protected backups, public rankings, optional consented Unity Analytics, AdMob rewarded ads where enabled, and verified store purchases where enabled. It does not assert that ads/payments are active.

Keep claims aligned with the release build and actual operations. Update the effective date when changing privacy practices. The owner selected a 90-day retention period for resolved support/deletion correspondence, subject to mandatory legal retention. Run that mailbox-retention process in practice. Add actual store links only once their listings exist; the homepage currently says the game is in development.

Private keys, OAuth secrets, service-account JSON, tokens, player exports, or support messages do not belong in this public repository.
