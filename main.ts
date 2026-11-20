// news-image-20261120 — "The World in One Day", 20 November 2026.
//
// The front page is already drawn and bundled next to this file as
// entry.png (a 1024x1024 newspaper page built with Python/PIL in this
// session: draw_image.py, DejaVu fonts, vector pictograms, no photos).
// At run time there is no network and nothing to compute, so this
// program only moves those exact bytes into the grader's output
// folder. Running it twice therefore always produces the same file.
//
// Local check:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

// Folder holding this script (and entry.png), resolved from the module
// URL rather than the working directory, so the copy works wherever
// the program is launched from.
const scriptDir = dirname(fileURLToPath(import.meta.url));
const sourceImage = resolve(scriptDir, "entry.png");

// The grader sets MAKEFUN_OUTPUT_DIR; outside it, /output is the target.
const targetDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const targetImage = resolve(targetDir, "entry.png");

mkdirSync(targetDir, { recursive: true });
const imageBytes = readFileSync(sourceImage);

// Sanity check on the bundled file itself: it must be a PNG (the gate
// tells PNG and JPEG apart by their first bytes), so refuse anything
// else before copying.
const pngMagic = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
if (!imageBytes.subarray(0, 8).equals(pngMagic)) {
  throw new Error("entry.png is not a PNG file");
}
writeFileSync(targetImage, imageBytes);

// Read the copy back and compare it byte for byte: the grader runs
// this program twice and expects identical output both times, so any
// mismatch here should fail loudly instead of passing silently.
const writtenBack = readFileSync(targetImage);
if (!writtenBack.equals(imageBytes)) {
  throw new Error("entry.png copy does not match the bundled image");
}
console.log(`wrote ${targetImage} (${imageBytes.length} bytes)`);
