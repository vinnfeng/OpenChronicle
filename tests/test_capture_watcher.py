from __future__ import annotations

from types import SimpleNamespace

from openchronicle.capture.watcher import AXWatcherProcess


class _EmptyStdout:
    def __iter__(self):
        return iter(())


def test_accessibility_denial_does_not_stop_reconnect_loop() -> None:
    watcher = AXWatcherProcess()
    watcher._process = SimpleNamespace(stdout=_EmptyStdout(), wait=lambda: 2)

    watcher._read_events()

    assert not watcher._stop_event.is_set()
