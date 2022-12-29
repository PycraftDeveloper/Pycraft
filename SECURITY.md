# Security Policy

## Supported Versions

Attached below is a table of all the different versions of Pycraft that can be found under the Branches section here: https://github.com/PycraftDeveloper/Pycraft/branches
This table represents which versions in the Branches section of the repository currently support security updates. The general rule is that the most recent non-developer release of Pycraft, and the most recent developer release of Pycraft will be supporting security patches, and any changes to improve security in these versions will be carried forward for as long as the vulnerability is present in newer supported versions and releases of Pycraft.

| Version | Supported          |
| ------- | ------------------ |
| 9.5.0   | :white_check_mark: |
| 9.5.1   | :x:                |
| 9.5.3   | :x:                |
| 9.5.4   | :x:                |
| 9.5.5   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability, please make us aware of the problem as soon as you can by choosing one or more of the options below:
* Creating a new issue in Pycraft's Issues tab (which you can find here: https://github.com/PycraftDeveloper/Pycraft/issues
  * If the issue you have identified does not currently cause problems* (or may do in future) then use the "security (caution)" label
  * If the issue you have identified is causing problems* then use the "security (warning)" label

* Let us know on social media:
  * Get in touch on Twitter at: https://twitter.com/PycraftDev
  * Get in touch on Discord at: https://discord.com/channels/929750166255321138/1056940430870183977

* Email us at: thomasjebbo@gmail.com

## Resolving a Vulnerability

Depending on if the "security (caution)" or "security (warning)" label is used will determine the scale and speed of our response.
If the problem* currently exists on a version of Pycraft we support security patches on, then we will:
* For the "caution" flag, add a notice to the ReadMe at the top, and issue a patch for this in the next developer version of Pycraft.
* For the "warning" flag, we will immediately start work on a fix for this problem for that version of Pycraft and all versions that precede it where that vulnerability is present.

If the problem* currently exists on a version of Pycraft we don’t support security patches on, then we will:
* In most cases issue a notice telling the user to avoid this version of Pycraft and give them a link to the latest safe version of Pycraft if one is available.
* In extreme cases we will either make changes to the source code to correct the problem, or we will make that version of Pycraft no longer available for download off our sites.

problem* - To us a _security_ problem is one where our work collects information from either the system or user without first asking for permission to do so. OR, when Pycraft attempts to connect to the internet for no clear reason. OR, when if a crash was to occur, it in some way makes other programs or systems unstable or vulnerable. OR, when a module releases a security focused patch (we will try and keep the requirements of Pycraft as up to date for each release as we can).
