from django.db import models
from .managers import MonitorManager


class Monitor(models.Model):
    """
    Class for URL Monitor

    Protocol Primer
            - ICMP:
                Response time
            - HTTP:
                DNS lookup time, connection time, time to first byte, and total response time
            - HTTPS:
                DNS lookup time, connection time, SSL handshake time, time to first byte, and total response time
    REGION_CHOICES
        - "USA1", "Oregan, USA"
        - "EU", "Frankfurt, Germany"
        - "USA2", "Ohio, USA"
        - "SEA", "Singapore"

    """

    PROTOCOL_CHOICES = (
        ("HTTP", "HTTP"),
        ("HTTPS", "HTTPS"),
        ("ICMP", "ICMP"),
    )

    FREQUENCY_CHOICES = (
        ("30", "30 Seconds"),
        ("60", "1 Minute"),
        ("300", "5 Minutes"),
        ("1800", "30 Minutes"),
        ("3600", "1 Hour"),
        ("21600", "6 Hour"),
    )

    # name for the model
    name = models.CharField(max_length=256, null=True, blank=True)
    # moved the validation to serializer
    protocol = models.CharField(max_length=8, choices=PROTOCOL_CHOICES, default="HTTPS")
    ip = models.GenericIPAddressField(default="127.0.0.1")
    # for port monitoring
    port = models.PositiveIntegerField(null=True, blank=True)
    timeout = models.PositiveIntegerField(default=5)
    # metadata region
    region_US1 = models.BooleanField(default=True)
    region_US2 = models.BooleanField(default=False)
    region_EU1 = models.BooleanField(default=False)
    region_Asia1 = models.BooleanField(default=False)
    # meta data
    last_checked = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    frequency = models.CharField(max_length=25, choices=FREQUENCY_CHOICES, default=30)
    # regex for mapping OK status
    regex = models.CharField(max_length=25, default="200")
    # custom model manager
    objects = MonitorManager()

    def __str__(self):
        return self.name


class MonitorResult(models.Model):
    """Monitor Results Class"""

    STATUS_CHOICES = (
        ("OK", "Status OK"),
        ("Down", "Status DOWN"),
        ("Unknown", "Unreachable"),
    )

    monitor = models.ForeignKey(
        Monitor, related_name="results", on_delete=models.CASCADE
    )
    # DNS lookup time
    dns_lookup_time = models.FloatField(null=True, default=True)
    # Connection time
    connection_time = models.FloatField(null=True, default=True)
    # SSL handshake time
    ssl_handshake_time = models.FloatField(null=True, default=True)
    # Total response time
    response_time = models.FloatField(null=True, blank=True)
    # Status
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default="Unknown")
    checked_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.status
