from tld import get_fld


def my_fld(domain):
    return get_fld(domain.strip(), fix_protocol=True, fail_silently=True)