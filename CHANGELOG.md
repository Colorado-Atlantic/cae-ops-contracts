# Changelog

## [0.5.0] — 2026-06-22

### Added
- `dispatch_change_log` — `ChangeLogEntry` / `ChangeLogResponse` for the trip
  dispatch change-log read endpoint (spec dispatch-change-log, PR #979).

## [0.4.0] — 2026-06-22

### Added
- `accounting` — `AccFeeTypesFlexRequest` / `AccFeeTypesFlexResponse` for the
  accessorial fee type registry admin routes (spec #95).

## [0.3.0] — 2026-06-20

### Added
- `paperwork` — paperwork/intake endpoint models (spec #101, ticket #1177):
  intake queue list/upload/search/assign + by-trip and by-week paperwork views.

## [0.2.0] — 2026-06-19

### Added
- `communications` — outgoing communications log models (spec #98)

## [0.1.0] — 2026-06-10

Initial extraction from `Colorado-Atlantic/scheduling` (`api/models/`).

### Added
- `errors` — shared `ApiError` / `FieldError` shapes (RFC 7807-aligned)
- `westbound` — WB API response models
- `eastbound` — EB API response models
- `eb_dispatch` — EB allocation console models
- `eb_metadata` — EB metadata models
- `eb_page_config` — EB page config models
- `eb_settings` — EB settings models
- `accounting` — accounting route models
- `accounting_page_config` — accounting page config models
- `admin_page_config` — admin page config models
- `address_aliases` — address alias models
- `location_hours` — location hours models
- `locations` — location models
- `segments` — segment models
- `misc` — miscellaneous shared models
- `wb_hud` — WB HUD models
