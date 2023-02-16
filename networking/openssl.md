# `OpenSSL`

## Generating Public & Private Keys

Notice that the key file generated contains the private key component and the public key component involved in the RSA algorithm. The length of the key pair file generated will not match the specified key size because the key size is the size of the private component contained in the key file. This can be inspected through `openssl rsa -in key.pem -noout -text`

- Key pair with key size 2048: `openssl genrsa -out key.pem 2048`
- Key pair with key size 4096 encrypted with AES128: `openssl genrsa -out key.pem -aes128 4096`

## Generate Certificates

To inspect the certificate, use `openssl x509 -in cert.pem -noout -text`

- Generate self-signed certificate: `openssl req -x509 -key key.pem -out cert.pem`
- Generate CSR: `openssl req -new -key key.pem -out csr.pem`

## Troubleshooting

- Inspect the certificate from a browser standpoint: `openssl s_client -connect ethancbanks.com:443`
- `ssldump`

## Reference

- [Using OpenSSL with Ed Harmoush 1/6 Generating Public & Private Keys](https://www.youtube.com/watch?v=17-GRHJ8I0s&list=PLtO_OYBiEo6kzs6dzPQ8CFilqZ6UxZKto)