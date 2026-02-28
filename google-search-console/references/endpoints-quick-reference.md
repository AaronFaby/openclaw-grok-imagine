# Google Search Console endpoint quick reference

Reference: https://developers.google.com/webmaster-tools/v1/api_reference_index

## Webmasters v3 base

`https://www.googleapis.com/webmasters/v3`

## 1) List verified sites

- Method: `GET`
- Path: `/sites`
- CLI: `gsc_cli.py sites`

## 2) Search Analytics query

- Method: `POST`
- Path: `/sites/{siteUrl}/searchAnalytics/query`
- Key request fields:
  - `startDate`, `endDate`
  - `dimensions[]` (`query`, `page`, `country`, `device`, `date`, ...)
  - `rowLimit`, `startRow`
  - `type` (`web`, `image`, `video`, `news`, `discover`, `googleNews`)
  - `dimensionFilterGroups`
- CLI: `gsc_cli.py analytics --site-url ... --start-date ... --end-date ...`

## 3) List sitemaps

- Method: `GET`
- Path: `/sites/{siteUrl}/sitemaps`
- CLI: `gsc_cli.py sitemaps --site-url ...`

## 4) URL Inspection helper (separate API)

- Base: `https://searchconsole.googleapis.com/v1`
- Method: `POST`
- Path: `/urlInspection/index:inspect`
- Body:
  - `inspectionUrl`
  - `siteUrl`
  - `languageCode`
- CLI: `gsc_cli.py inspect --site-url ... --inspection-url ...`

## URL encoding note

`siteUrl` must be URL-encoded in Webmasters v3 paths. The helper script handles encoding automatically.
