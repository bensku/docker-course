# Use multi-stage build, we don't need GCC in final image
FROM alpine as builder

# Install build tools we need
RUN apk add --no-cache build-base curl tar unzip openssl openssl-dev

# Build Lua 5.4
RUN curl https://www.lua.org/ftp/lua-5.4.2.tar.gz >lua.tar.gz && tar xkf lua.tar.gz
WORKDIR /lua-5.4.2
RUN make all test
RUN mkdir /lua-install && make install INSTALL_TOP=/lua-install

# Build Luarocks, we'll install a few packages
# (not included in final image, most packages need a C compiler)
WORKDIR /
RUN curl -L https://luarocks.org/releases/luarocks-3.3.1.tar.gz >luarocks.tar.gz
RUN tar xkf luarocks.tar.gz
WORKDIR /luarocks-3.3.1
RUN ./configure --with-lua=/lua-install
RUN make
RUN make install

# Install select modules
WORKDIR /
RUN luarocks install --tree rocks lua-cjson 2.1.0-1
RUN luarocks install --tree rocks luafilesystem
RUN luarocks install --tree rocks luasocket
RUN luarocks install --tree rocks luasec

FROM alpine

# Dependencies needed by Lua or libraries
RUN apk add --no-cache openssl

# Copy Lua binaries, libraries, etc.
COPY --from=builder /lua-install /opt/lua
COPY --from=builder /rocks /opt/lua-rocks

# Configure executable and library paths
ENV PATH "$PATH:/opt/lua/bin"
ENV LD_LIBRARY_PATH "$PATH:/opt/lua/"
ENV LUA_PATH "/opt/lua-rocks/share/lua/5.4/?.lua;/opt/lua-rocks/share/lua/5.4/?/init.lua;;"
ENV LUA_CPATH "/opt/lua-rocks/lib/lua/5.4/?.so;;"

# Don't run as root
RUN addgroup -S lua && adduser -S lua -G lua
USER lua
WORKDIR /home/lua
CMD [ "lua" ]