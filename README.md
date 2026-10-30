# Test Files for Internet Speed Test

Binary files of different sizes for Internet speed testing through raw GitHub URLs.

Files are stored using **Git LFS** (Large File Storage). Each `*.bin` file is random data from `generate.py` (`os.urandom`, written in chunks). Sizes are powers of two mebibytes: 1 MiB = 1024 × 1024 bytes.

## Available files

| File | Size | Bytes | Raw URL | Media URL |
|------|------|------:|---------|-----------|
| 8MB.bin | 8 MiB | 8388608 | https://github.com/ExploiTR/speed-test-files/raw/main/8MB.bin | https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/8MB.bin |
| 16MB.bin | 16 MiB | 16777216 | https://github.com/ExploiTR/speed-test-files/raw/main/16MB.bin | https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/16MB.bin |
| 32MB.bin | 32 MiB | 33554432 | https://github.com/ExploiTR/speed-test-files/raw/main/32MB.bin | https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/32MB.bin |
| 64MB.bin | 64 MiB | 67108864 | https://github.com/ExploiTR/speed-test-files/raw/main/64MB.bin | https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/64MB.bin |
| 128MB.bin | 128 MiB | 134217728 | https://github.com/ExploiTR/speed-test-files/raw/main/128MB.bin | https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/128MB.bin |
| 256MB.bin | 256 MiB | 268435456 | https://github.com/ExploiTR/speed-test-files/raw/main/256MB.bin | https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/256MB.bin |
| 512MB.bin | 512 MiB | 536870912 | https://github.com/ExploiTR/speed-test-files/raw/main/512MB.bin | https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/512MB.bin |
| 1GB.bin | 1024 MiB | 1073741824 | https://github.com/ExploiTR/speed-test-files/raw/main/1GB.bin | https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/1GB.bin |
| 2GB.bin | 2048 MiB | 2147483648 | https://github.com/ExploiTR/speed-test-files/raw/main/2GB.bin | https://media.githubusercontent.com/media/ExploiTR/speed-test-files/main/2GB.bin |

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
