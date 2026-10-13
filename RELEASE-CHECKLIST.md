# Fishito release website handoff

The website supplies public pages and a request-by-email route. It is not an assertion that the game or external services have passed release review.

## Website and listings

- [ ] Check all public HTTPS URLs in README on desktop and a phone.
- [ ] Put the developer website, privacy policy, support, deletion URL, and public contact email into the matching store fields.
- [ ] Match the developer name **Lephron Games** to the store listing or update the site to the actual publisher name.
- [ ] Add privacy/support/deletion links to the game where required. The current game Settings privacy button links to Unity's analytics policy, which does not replace Fishito's own policy. Preserve that useful provider link and add the game policy separately.
- [ ] Decide the release target audience and set the store/ad SDK audience treatment to match. The website deliberately does not invent an age rating or claim child-directed compliance.
- [ ] Complete Google Data safety and Apple App Privacy using the **actual shipped SDKs and settings**, including account/player IDs, public names/photos/rankings, purchase verification, network/device data, and optional analytics/ads. Consent does not remove disclosure obligations.
- [ ] Replace the development message with real store links at launch.

## AdMob — blocked until publisher entry is supplied

- [ ] Paste the owner's personalized AdMob entry into root `app-ads.txt`; do not put it only in a game subdirectory.
- [ ] Run `python3 scripts/check_site.py --require-ads` and verify the live file contains the same entry.
- [ ] Link published store listings and request AdMob verification/readiness review.
- [ ] Configure applicable UMP messages, audience treatment and iOS tracking permissions; verify on physical devices.
- [ ] Replace sample app/unit IDs and enable live ads only after the device checks in Fishito's `Docs/Ads.md` pass.

## Manual account/data deletion — operational checks before release

The public page starts an email request; it does not delete records itself. Fishito currently has analytics deletion but no full account-deletion endpoint or in-game account-deletion action. The operator must make this process work end to end, and provide the required in-game route before claiming account-deletion compliance. Review the current platform rules for the chosen login/account flow.

1. Monitor `lephron.studios@gmail.com`. Receive the request without requiring the app to be installed or a new login to the website.
2. Establish a reliable ownership-verification process. A username, screenshot, email address, or knowledge of a leaderboard score alone is not authentication. Do not ask for passwords, codes, OAuth tokens or payment-card information. Add an authenticated in-game support/verification mechanism if existing admin tools cannot establish the requester owns the relevant Unity player.
3. Locate the exact Unity player and all linked records. Confirm the requested scope and explain the irreversible loss of progress/consumed purchases before executing deletion. Do not use a local New Game reset as deletion.
4. In authorized Unity admin tools, remove the Protected `fishito_save` record (including profile, daily-claim ledger and purchase ledger), the player's entries and metadata from `fishito_depth`, `fishito_collection`, `fishito_level`, and the Authentication player. Check for additional service records. Do not assume deleting Authentication automatically clears other services.
5. Handle analytics separately: the Unity SDK uses its own analytics identifiers. Exercise the current in-game deletion request; establish the provider-supported identity/recovery path for a requester who uninstalled. Test this using disposable accounts rather than guessing that a Unity Authentication deletion removes analytics.
6. Explain local-device cleanup. An old signed local save may repopulate a new cloud account if the player reconnects; deleting online records does not wipe devices. Google/Apple platform accounts and store-held payment records are independent.
7. Confirm completion only after verifying all requested records are removed, or clearly explain any legally required retention and its duration. Do not retain the game purchase/daily ledgers for convenience after promising full deletion. Any anti-fraud retention change requires a policy update with retained categories/reasons/period.
8. Delete resolved support and deletion-request emails/attachments after **90 days**, except any specifically applicable mandatory retention. Handle recoverable copies as appropriate to the mailbox/provider process. Keep legal retention exceptions limited and explained to the requester.

Validate this flow with a disposable, authenticated device account **before store submission**. The website does not guarantee provider deletion completion, Apple acceptance of a manual-only process, or a successful store review.

## Existing game/service release work

Follow the game repository's `Docs/CloudSaveSetup.md`, `Docs/Leaderboard.md`, `Docs/DailyRewards.md`, `Docs/Analytics.md`, `Docs/Ads.md` and `Docs/Shop.md`. Google Play Games credentials, real-device sign-in/restore, Unity Analytics dashboard schemas, AdMob activation, and store products/server secrets remain separate from publishing this website.

## Official references

- Google privacy and review setup: https://support.google.com/googleplay/android-developer/answer/9859455?hl=en
- Google account deletion: https://support.google.com/googleplay/android-developer/answer/13327111?hl=en
- Apple account deletion: https://developer.apple.com/support/offering-account-deletion-in-your-app/
- Google Mobile Ads data disclosure: https://developers.google.com/admob/unity/privacy/play-data-disclosure
- Unity Analytics privacy/deletion: https://docs.unity.com/en-us/analytics/privacy-and-consent/manage-data-privacy
- AdMob seller setup: https://support.google.com/admob/answer/9363762?hl=en
