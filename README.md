# Test Files for Internet Speed Test

Binary files of different sizes for Internet speed testing through raw GitHub URLs.

Files are stored using **Git LFS** (Large File Storage). Each `*.bin` file is random data from `generate.py` (`os.urandom`, written in chunks). Sizes are powers of two mebibytes: 1 MiB = 1024 × 1024 bytes.

## Available files

| File | Size | Bytes | MD5 | SHA-256 | Raw URL | Media URL |
|------|------|------:|-----|---------|---------|-----------|
| 8MB.bin | 8 MiB | 8388608 | `95d6b652f5d4ad43160a59d0a10ac23f` | `7158d8660edf9f369f24fd05592d00dbe4906284d09378d8717b07ee2cba939c` | https://github.com/ExploiTR/speed-test-files/raw/main/8MB.bin | https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/8MB.bin |
| 16MB.bin | 16 MiB | 16777216 | `602eeb3a33a7f9822e01728391c28306` | `d345ecd66c643524718aae5f2dba3c0d0b3c573d489620ee02bc92743ecf576e` | https://github.com/ExploiTR/speed-test-files/raw/main/16MB.bin | https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/16MB.bin |
| 32MB.bin | 32 MiB | 33554432 | `f84229b4c4720c08b4273236e584e123` | `e2e629a71083e4a7ea74392034d0b21692769f0549c82ca7a53193093ce95c0c` | https://github.com/ExploiTR/speed-test-files/raw/main/32MB.bin | https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/32MB.bin |
| 64MB.bin | 64 MiB | 67108864 | `eed3fcffc18347f54117b82062bd4bdd` | `a44455d30c7cc207859f41fc3de1d04ba5d55e74592b7ecd0095bd18da593500` | https://github.com/ExploiTR/speed-test-files/raw/main/64MB.bin | https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/64MB.bin |
| 128MB.bin | 128 MiB | 134217728 | `95bb542b904358e93105fe5307017b80` | `7ecb09066ef94c7cb7061b4588aa8ed6a022758e6e1705a301923a7584a1b53d` | https://github.com/ExploiTR/speed-test-files/raw/main/128MB.bin | https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/128MB.bin |
| 256MB.bin | 256 MiB | 268435456 | `315a503ab918e8d7308598c7998dd9d0` | `07ecbbc2a76a5defb71f8798eef146a4bc2352e562542cccaa78eb09eb4f235e` | https://github.com/ExploiTR/speed-test-files/raw/main/256MB.bin | https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/256MB.bin |
| 512MB.bin | 512 MiB | 536870912 | `4b7d63105206771d8d462943f1d1e9d8` | `1a0dfef59c6b3eea987a2a3bbb0dde2aa6e9e98e10159b05b5cad82f0e377b8b` | https://github.com/ExploiTR/speed-test-files/raw/main/512MB.bin | https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/512MB.bin |
| 1GB.bin | 1024 MiB | 1073741824 | `ea7e7472aad69088c62db7eb01b48488` | `7fcc583d265b7cdb7234021dd336ef8ef78a99804f87ffbc9c3742e842113839` | https://github.com/ExploiTR/speed-test-files/raw/main/1GB.bin | https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/1GB.bin |
| 2GB.bin | 2048 MiB | 2147483648 | `222ba423447a75e75d5c88fe10e83206` | `aaa56598975725595401ace58b76b9e19c71aa02658c5b890105384215d4daee` | https://github.com/ExploiTR/speed-test-files/raw/main/2GB.bin | https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/2GB.bin |

SHA-256 matches the Git LFS object id. To check one download:

```bash
echo '95d6b652f5d4ad43160a59d0a10ac23f *8MB.bin' | md5sum -c
```

Or save this block as `checksums.md5` and run `md5sum -c checksums.md5` in the download directory:

```
95d6b652f5d4ad43160a59d0a10ac23f *8MB.bin
602eeb3a33a7f9822e01728391c28306 *16MB.bin
f84229b4c4720c08b4273236e584e123 *32MB.bin
eed3fcffc18347f54117b82062bd4bdd *64MB.bin
95bb542b904358e93105fe5307017b80 *128MB.bin
315a503ab918e8d7308598c7998dd9d0 *256MB.bin
4b7d63105206771d8d462943f1d1e9d8 *512MB.bin
ea7e7472aad69088c62db7eb01b48488 *1GB.bin
222ba423447a75e75d5c88fe10e83206 *2GB.bin
```

## Copy prompt for testing

Paste this into an assistant to run a download speed test:

```text
Run a download speed test with these files, smallest first. For each file, download the media URL (it returns the real bytes, not a Git LFS pointer), measure the time, report speed in MB/s and Mbps, and verify the MD5. Stop at a sensible size for this connection: skip larger files if the link is slow, data is limited, or the previous file already took long enough to measure. Delete the downloads when you are done. Report a table with file, bytes, seconds, MB/s, Mbps, and MD5 (ok or mismatch).

8MB.bin — 8 MiB, 8388608 bytes — MD5 95d6b652f5d4ad43160a59d0a10ac23f — https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/8MB.bin
16MB.bin — 16 MiB, 16777216 bytes — MD5 602eeb3a33a7f9822e01728391c28306 — https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/16MB.bin
32MB.bin — 32 MiB, 33554432 bytes — MD5 f84229b4c4720c08b4273236e584e123 — https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/32MB.bin
64MB.bin — 64 MiB, 67108864 bytes — MD5 eed3fcffc18347f54117b82062bd4bdd — https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/64MB.bin
128MB.bin — 128 MiB, 134217728 bytes — MD5 95bb542b904358e93105fe5307017b80 — https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/128MB.bin
256MB.bin — 256 MiB, 268435456 bytes — MD5 315a503ab918e8d7308598c7998dd9d0 — https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/256MB.bin
512MB.bin — 512 MiB, 536870912 bytes — MD5 4b7d63105206771d8d462943f1d1e9d8 — https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/512MB.bin
1GB.bin — 1024 MiB, 1073741824 bytes — MD5 ea7e7472aad69088c62db7eb01b48488 — https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/1GB.bin
2GB.bin — 2048 MiB, 2147483648 bytes — MD5 222ba423447a75e75d5c88fe10e83206 — https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/2GB.bin
```

## How to download files

Since files are stored with Git LFS, the raw GitHub URL returns a **redirect to the actual file content**. Use the `media` endpoint or follow redirects.

### Direct download URL (recommended)

```
https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/<FILE>
```

Example:

```
https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/8MB.bin
https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/128MB.bin
https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/1GB.bin
```

### Alternative: raw URL with redirect

```
https://github.com/ExploiTR/speed-test-files/raw/main/<FILE>
```

Example:

```
https://github.com/ExploiTR/speed-test-files/raw/main/8MB.bin
```

> **Note:** Some clients (like `fetch` in browsers) follow the redirect automatically. If you get a small text file instead of the binary, you're getting the LFS pointer — use the `media` URL instead.

### Example commands

`curl` needs `-L` so it follows the LFS redirect. `wget` follows redirects by default.

```bash
curl -L -o 8MB.bin https://github.com/ExploiTR/speed-test-files/raw/main/8MB.bin
wget -O 8MB.bin https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/8MB.bin
```

```bash
curl -L -o 1GB.bin https://github.com/ExploiTR/speed-test-files/raw/main/1GB.bin
wget -O 2GB.bin https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/2GB.bin
```

### Clone with Git LFS

To clone the full repository with all binary files:

```bash
git lfs install
git clone https://github.com/ExploiTR/speed-test-files.git
```

### Regenerating the files

```bash
python3 generate.py
```
