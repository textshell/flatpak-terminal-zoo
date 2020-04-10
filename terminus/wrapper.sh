#! /bin/bash

# eleminate state
STATEDIR="$(mktemp --directory)"

mkdir "$STATEDIR/terminus"
cp /app/config.yaml "$STATEDIR/terminus"

export XDG_CONFIG_HOME="$STATEDIR"

# discard possible -e
shift
if [ -n "$1" ] ; then
    # terminus does not allow running commands from commandline if not already running, fake it.
    echo "#! /bin/bash" > "$STATEDIR/run.sh"
    echo "/bin/bash -c '$@'" >> "$STATEDIR/run.sh"
    echo "touch $STATEDIR/terminated" >> "$STATEDIR/run.sh"
    echo "pkill -TERM --oldest terminus.bin" >> "$STATEDIR/run.sh"
    chmod a+x "$STATEDIR/run.sh"
    sed -i -e "s#/bin/bash#$STATEDIR/run.sh#" "$STATEDIR/terminus/config.yaml"
fi

/app/bin/terminus.bin --no-sandbox
RET=$?

if [ -f "$STATEDIR/terminated" ] ; then
    RET=0
fi

exit $RET
