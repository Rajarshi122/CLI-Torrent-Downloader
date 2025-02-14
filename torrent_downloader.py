import libtorrent as lt
import time
import sys
import os

def download_torrent(magnet_link, save_path='./Downloads'):
    os.makedirs(save_path, exist_ok=True)
    ses = lt.session()


    settings = {
        'user_agent': f'python-libtorrent/{lt.__version__}',
        'peer_fingerprint': lt.generate_fingerprint('LT', 2, 0, 10, 0)
    }
    ses.apply_settings(settings)
    params = lt.add_torrent_params()
    params.save_path = save_path
    params.storage_mode = lt.storage_mode_t.storage_mode_sparse
    
    if magnet_link.startswith('magnet:'):
        parsed = lt.parse_magnet_uri(magnet_link)
        params.info_hash = parsed.info_hash
        params.trackers = parsed.trackers
        params.name = parsed.name
        params.url = magnet_link
    else:
        params.ti = lt.torrent_info(magnet_link)
    


    handle = ses.add_torrent(params)
    
    while not handle.status().has_metadata:  
        time.sleep(1)
    
    print(f"Starting download: {handle.status().name}")
    
    while not handle.status().is_seeding:
        s = handle.status()
        print(f"\rProgress: {s.progress * 100:.2f}% | Speed: {s.download_rate / 1024:.1f} kB/s", end='')
        time.sleep(1)
    
    print("\nDownload complete!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python TorrentDn.py <magnet/torrent> [save_path]")
        sys.exit(1)
    
    save_path = sys.argv[2] if len(sys.argv) > 2 else './downloads'
    download_torrent(sys.argv[1], save_path)
