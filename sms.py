"""Optional SMS via Twilio. Silently no-ops if env vars not set."""
import os
import logging

log = logging.getLogger(__name__)


def send_sms(to: str, body: str) -> bool:
    sid = os.environ.get("TWILIO_ACCOUNT_SID")
    token = os.environ.get("TWILIO_AUTH_TOKEN")
    from_num = os.environ.get("TWILIO_PHONE_NUMBER")

    if not (sid and token and from_num and to):
        log.info(
            "[SMS-LOG] (twilio not configured) to=%s body=%s",
            to,
            body,
        )
        return False

    try:
        from twilio.rest import Client

        Client(
            sid,
            token
        ).messages.create(
            body=body,
            from_=from_num,
            to=to,
        )

        return True

    except Exception as e:
        log.warning(
            "Twilio send failed: %s",
            e,
        )
        return False